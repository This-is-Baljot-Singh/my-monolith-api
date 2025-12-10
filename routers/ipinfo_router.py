from fastapi import APIRouter, HTTPException
import requests

router = APIRouter(prefix="/ipinfo", tags=["IP Info"])

@router.get("/{ip_address}")
def get_ip_info(ip_address: str):
    """Fetch geographical and network information about an IP address using ipinfo.io"""
    url = f"https://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if "error" in data:
            raise HTTPException(status_code=404, detail=data["error"])
        return data
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail="Failed to fetch IP info") from e
