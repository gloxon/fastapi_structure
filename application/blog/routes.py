from fastapi import APIRouter


router = APIRouter(
    prefix="/blog",
    tags = ["blot"], 
    dependencies = []
)

