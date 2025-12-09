from fastapi import APIRouter, Query
import string
import random

router = APIRouter(prefix="/passwordgenerator", tags=["Password Generator"])

@router.get("/generate")
def generate_password(length: int = Query(12, ge=6, le=64), use_special: bool = True):
    """Generate a random password with given length and optional special characters."""
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += "!@#$%^&*()-_=+[]{}|;:,.<>?"
    password = ''.join(random.choice(chars) for _ in range(length))
    return {"password": password, "length": length, "use_special": use_special}
