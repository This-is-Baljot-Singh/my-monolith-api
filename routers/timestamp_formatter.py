from fastapi import APIRouter, Query
from datetime import datetime
from typing import Optional

router = APIRouter(prefix="/timestamp_formatter", tags=["Timestamp Formatter"])

@router.get("/format")
def format_timestamp(
    timestamp: Optional[int] = Query(None, description="Unix timestamp in seconds. If not provided, current time is used."),
    fmt: str = Query("%Y-%m-%d %H:%M:%S", description="Datetime format string using Python's strftime directives")
):
    """Format a Unix timestamp into a human-readable string."""
    dt = datetime.fromtimestamp(timestamp) if timestamp is not None else datetime.now()
    try:
        formatted = dt.strftime(fmt)
    except Exception as e:
        return {"error": "Invalid format string", "detail": str(e)}
    return {"formatted_timestamp": formatted, "original_timestamp": int(dt.timestamp())}
