from fastapi import APIRouter
from sqlalchemy import func

from database.db import SessionLocal
from database.models import NewsPost

router = APIRouter()