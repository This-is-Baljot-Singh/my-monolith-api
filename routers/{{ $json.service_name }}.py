import io
import base64
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

# Note: The 'qrcode' library is allowed per the task requirements.
import qrcode
import qrcode.constants

# Define the APIRouter
router = APIRouter(
    prefix="/qr_code",
    tags=["QR Code Generator"]
)


@router.get("/generate", response_model=dict)
async def generate_qr_code(
    text: str,
    box_size: int = 10,
    border: int = 4
):
    """
    Generates a QR Code image based on the provided text, returning the image as a Base64 encoded string (PNG format).
    
    Query Parameters:
    - text: The data to be encoded in the QR code (Required).
    - box_size: The size of each box (pixel) in the QR code grid (Default: 10).
    - border: The thickness of the border (Default: 4).
    """
    if not text:
        raise HTTPException(status_code=400, detail="Text parameter cannot be empty.")

    try:
        # 1. Create the QR code object
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )
        qr.add_data(text)
        qr.make(fit=True)

        # Create the image
        img = qr.make_image(fill_color="black", back_color="white")

        # 2. Save the image to an in-memory buffer (BytesIO)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # 3. Encode the buffer content to Base64
        base64_encoded_image = base64.b64encode(buffer.read()).decode('utf-8')

        return JSONResponse(content={
            "text": text,
            "box_size": box_size,
            "image_format": "png",
            "base64_image": base64_encoded_image,
            "data_uri": f"data:image/png;base64,{base64_encoded_image}"
        })

    except Exception as e:
        # Catch unexpected errors during generation
        raise HTTPException(status_code=500, detail=f"Error generating QR code: {type(e).__name__}: {str(e)}")