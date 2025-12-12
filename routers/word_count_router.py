from fastapi import APIRouter, Query
from typing import Optional

router = APIRouter(prefix="/wordcount", tags=["Word Count"])

@router.get("/count")
async def count_words(text: Optional[str] = Query(None, description="Text to count words in")):
    if not text or text.isspace():
        return {"word_count": 0, "character_count": 0}
    words = text.strip().split()
    return {"word_count": len(words), "character_count": len(text)}
