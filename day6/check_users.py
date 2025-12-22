import asyncio
from app.db.session import AsyncSessionLocal
from app.models.user import User
from sqlalchemy import select

async def list_users():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        print(f"Total Users: {len(users)}")
        for u in users:
            print(f"- {u.email} (Active: {u.is_active})")

if __name__ == "__main__":
    asyncio.run(list_users())
