from typing import List, Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.paper import Paper
from src.schemas.paper import PaperCreate

