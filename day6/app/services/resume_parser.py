import PyPDF2
import io
import re
from typing import Dict, List, Any

class ResumeParser:
    @staticmethod
    def extract_text_from_pdf(file_content: bytes) -> str:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_content))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

    @staticmethod
    def parse_resume(text: str) -> Dict[str, Any]:
        # Very basic regex-based extraction
        # In a real app, this would be much more sophisticated (or use LLM)
        portfolio_data = {
            "bio": "",
            "skills": [],
            "experience": [],
            "education": [],
            "projects": [],
            "social_links": {}
        }

        # Look for skills
        skills_match = re.search(r'(?i)skills:?(.*?)(\n\n|\n[A-Z]|$)', text, re.DOTALL)
        if skills_match:
            skills_text = skills_match.group(1).strip()
            # Split by common separators
            portfolio_data["skills"] = [s.strip() for s in re.split(r'[,|•\n]', skills_text) if s.strip()]

        # Look for experience (just capturing the whole block for now)
        exp_match = re.search(r'(?i)experience:?(.*?)(\n\n|\n[A-Z]|$)', text, re.DOTALL)
        if exp_match:
            exp_text = exp_match.group(1).strip()
            portfolio_data["experience"] = [{"description": exp_text}]

        # Look for education
        edu_match = re.search(r'(?i)education:?(.*?)(\n\n|\n[A-Z]|$)', text, re.DOTALL)
        if edu_match:
            edu_text = edu_match.group(1).strip()
            portfolio_data["education"] = [{"description": edu_text}]

        # Set a default bio if nothing else
        lines = text.split('\n')
        if lines:
            portfolio_data["bio"] = f"Professional portfolio for {lines[0].strip()}"

        return portfolio_data
