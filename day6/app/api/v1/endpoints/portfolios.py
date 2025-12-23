from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Any
import uuid

from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.models.portfolio import Portfolio
from app.schemas.portfolio import PortfolioCreate, PortfolioUpdate, PortfolioResponse
from app.services.resume_parser import ResumeParser

router = APIRouter()

@router.post("/generate-from-resume", response_model=PortfolioResponse)
async def generate_from_resume(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Generate portfolio data from a resume (PDF).
    """
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are supported"
        )
    
    content = await file.read()
    try:
        text = ResumeParser.extract_text_from_pdf(content)
        parsed_data = ResumeParser.parse_resume(text)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error parsing resume: {str(e)}"
        )
    
    # Check if user already has a portfolio
    result = await db.execute(select(Portfolio).filter(Portfolio.user_id == current_user.id))
    existing_portfolio = result.scalars().first()
    
    if existing_portfolio:
        # Update existing
        for key, value in parsed_data.items():
            setattr(existing_portfolio, key, value)
        portfolio = existing_portfolio
    else:
        # Create new
        portfolio = Portfolio(
            user_id=current_user.id,
            **parsed_data
        )
        db.add(portfolio)
    
    await db.commit()
    await db.refresh(portfolio)
    return portfolio

@router.post("/save", response_model=PortfolioResponse)
async def save_portfolio(
    portfolio_in: PortfolioCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Save or update manually filled portfolio details.
    """
    result = await db.execute(select(Portfolio).filter(Portfolio.user_id == current_user.id))
    portfolio = result.scalars().first()
    
    if portfolio:
        update_data = portfolio_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(portfolio, key, value)
    else:
        portfolio = Portfolio(
            user_id=current_user.id,
            **portfolio_in.model_dump()
        )
        db.add(portfolio)
    
    await db.commit()
    await db.refresh(portfolio)
    return portfolio

@router.get("/me", response_model=PortfolioResponse)
async def get_my_portfolio(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Get current user's portfolio.
    """
    result = await db.execute(select(Portfolio).filter(Portfolio.user_id == current_user.id))
    portfolio = result.scalars().first()
    if not portfolio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Portfolio not found for this user"
        )
    return portfolio
