from datetime import datetime
from typing import List
from uuid import UUID
from pydantic import BaseModel, Field

class PaperBase(BaseModel):
    arxiv_id: str = Field(..., description="Arxiv paper ID")
    title: str = Field(..., description="Paper Title")
    authors: List[str] = Field(..., description="List of authors names")
    abstract: str = Field(..., description="Paper Abstract")
    categories: List[str] = Field(..., description="List of categories names")
    publication_date: datetime = Field(..., description="Paper publication date")
    pdf_url: str = Field(..., description="Paper PDF URL")

class PaperCreate(PaperBase):
    pass

class PaperResponse(PaperBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class PaperSearchResponse(BaseModel):
    papers: List[PaperResponse]
    total: int