from apis.s3_api import router as s3_router
from fastapi import FastAPI


app: FastAPI = FastAPI()


app.include_router(s3_router, prefix="/s3", tags=["s3 minio"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
