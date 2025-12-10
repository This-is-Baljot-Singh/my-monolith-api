from fastapi import APIRouter, Query, Response
import qrcode
from io import BytesIO

router = APIRouter(prefix="/qr_code_generator", tags=["QR Code Generator"])

@router.get("/generate")
async def generate_qr_code(data: str = Query(..., description="Data to encode in the QR code")):
    """Generate a QR code image from the provided data and return it as PNG."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return Response(content=buffer.read(), media_type="image/png")