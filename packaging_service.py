from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.post("/package")
def package(product: dict):
    return {
        "stage": "Packaging",
        "message": f"Packaging completed for {product['productName']}"
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
