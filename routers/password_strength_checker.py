from fastapi import APIRouter, Query, HTTPException
import re

router = APIRouter(prefix="/password_strength", tags=["Password Strength"])

@router.get("/check")
async def check_password_strength(password: str = Query(..., min_length=1)):
    """Check the strength of a given password and return a strength score and details."""

    # Define criteria
    length_criteria = len(password) >= 8
    lower_criteria = bool(re.search(r"[a-z]", password))
    upper_criteria = bool(re.search(r"[A-Z]", password))
    digit_criteria = bool(re.search(r"\d", password))
    special_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    score = sum([length_criteria, lower_criteria, upper_criteria, digit_criteria, special_criteria])

    strength_levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }

    details = {
        "length_at_least_8": length_criteria,
        "has_lowercase": lower_criteria,
        "has_uppercase": upper_criteria,
        "has_digit": digit_criteria,
        "has_special_char": special_criteria
    }

    return {
        "password": password,
        "score": score,
        "strength": strength_levels[score],
        "criteria_details": details
    }