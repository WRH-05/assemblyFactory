from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.post("/assemble")
def assemble(product: dict):
    return {
        "stage": "Assembly",
        "message": f"Assembly completed for {product['productName']}"
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://assembly-factory.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)
