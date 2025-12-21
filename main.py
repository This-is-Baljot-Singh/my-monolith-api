
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# --- IMPORTS ---
# The automation will inject new module imports below this line.
from routers import health_check
from routers import timestamp_formatter
from routers import hex_color_generator
from routers import random_password_generator
from routers import password_strength_checker
from routers import uuid_generator
from routers import qr_code_generator
from routers import ipinfo_router
from routers import word_count_router
from routers import random_number_generator
# IMPORT_ANCHOR - Do not delete

app = FastAPI(
    title="The Monolith API",
    description="A centralized hub for all my automated micro-services.",
    version="1.0.0"
)

# --- CORS SETUP ---
# Allows RapidAPI and other frontends to access your API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "status": "online",
        "message": "The Monolith is operational. Visit /docs for endpoints."
    }

# --- ROUTER INCLUSION ---
# The automation will inject new router inclusions below this line.
app.include_router(health_check.router)
app.include_router(timestamp_formatter.router)
app.include_router(hex_color_generator.router)
app.include_router(random_password_generator.router)
app.include_router(password_strength_checker.router)
app.include_router(uuid_generator.router)
app.include_router(qr_code_generator.router)
app.include_router(ipinfo_router.router)
app.include_router(word_count_router.router)
app.include_router(random_number_generator.router)
# INCLUDE_ANCHOR - Do not delete

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
