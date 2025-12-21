from fastapi import APIRouter, Query

router = APIRouter(prefix="/text_reverser", tags=["Text Reverser"])

@router.get("/reverse")
async def reverse_text(text: str = Query(..., description="Text to be reversed")):
    """Reverse the input string and return it."""
    reversed_text = text[::-1]
    return {"original": text, "reversed": reversed_text}
