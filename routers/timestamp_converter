from fastapi import APIRouter, Query
from datetime import datetime, timezone, timedelta
from typing import Optional

router = APIRouter(prefix="/timestamp_converter", tags=["Timestamp Converter"])

@router.get("/convert")
async def convert_timestamp(
    timestamp: int = Query(..., description="Unix timestamp to convert"),
    to_timezone: Optional[str] = Query("UTC", description="Target timezone in ±HH:MM format, e.g. +03:00 or -05:30")
):
    """
    Convert a Unix timestamp to an ISO8601 datetime string in the target timezone.
    """
    try:
        # Parse timezone offset
        if to_timezone.upper() == "UTC":
            tz = timezone.utc
        else:
            sign = 1 if to_timezone[0] == '+' else -1
            parts = to_timezone[1:].split(":")
            if len(parts) != 2:
                return {"error": "Invalid timezone format. Use ±HH:MM or UTC."}
            hours = int(parts[0])
            minutes = int(parts[1])
            offset = timedelta(hours=hours, minutes=minutes) * sign
            tz = timezone(offset)
    except Exception:
        return {"error": "Invalid timezone format. Use ±HH:MM or UTC."}

    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    dt_target = dt.astimezone(tz)

    return {
        "original_timestamp": timestamp,
        "original_datetime_utc": dt.isoformat(),
        "converted_datetime": dt_target.isoformat(),
        "target_timezone": to_timezone
    }
