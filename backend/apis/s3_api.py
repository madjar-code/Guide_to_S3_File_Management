from fastapi import APIRouter, HTTPException, Query, status

from schemas import MessageResponseSchemaOut
from schemas import (
    DownloadTestFileSchemaOut,
    DownloadLinkSchemaOut,
    UploadTestFileSchemaOut,
    UploadUrlSchemaOut,
)
from exceptions import S3ObjectDoesntExistException
from services.minio_s3_service import S3Service


router = APIRouter()


@router.post("/upload-test-file-to-s3")
async def upload_test_file_to_s3() -> UploadTestFileSchemaOut:
    """
    Test route to upload a file ./test_upload_file.txt to S3. File must exist.
    ---
    Attention. This route is only for demonstation purposes. No need is such route in production
    application.
    """
    s3_service: S3Service = S3Service()
    s3_object_path: str = s3_service.upload("test_upload_file.txt")
    return UploadTestFileSchemaOut(s3_object_path=s3_object_path)


@router.get("/download-file-from-s3/")
async def download_file_from_s3(
    s3_object_path: str = Query(..., example="2024/12/27/123.txt"),
) -> DownloadTestFileSchemaOut:
    """
    Test route to download a file from S3.
    ---
    Attention. This route is only for demonstration purposes. No need in such route in production
    application.
    """
    s3_service: S3Service = S3Service()
    try:
        download_file_path: str = s3_service.download(s3_object_path)
    except S3ObjectDoesntExistException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return DownloadTestFileSchemaOut(downloaded_file_path=download_file_path)


@router.delete("/delete-file-from-s3/")
async def remove_file_from_s3(
   s3_object_path: str = Query(..., example="2024/12/27/123.txt"),
) -> MessageResponseSchemaOut:
   """
   Test route to delete a file from S3 storage.
   ---
   Attention. This route is only for demonstration purposes. No need in such route in production
   application.
   """
   s3_service: S3Service = S3Service()
   try:
       s3_service.remove_digital_object(s3_object_path)
   except S3ObjectDoesntExistException:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
   return MessageResponseSchemaOut(message="File deleted")


@router.get("/s3-upload-url")
async def generate_presigned_upload_url() -> UploadUrlSchemaOut:
   """Generate presigned url for file upload directly to S3 storage."""
   s3_service: S3Service = S3Service()
   url, s3_object_path = s3_service.generate_presigned_upload_url()
   return UploadUrlSchemaOut(url=url, s3_object_path=s3_object_path)


@router.get("/s3-download-url")
async def generate_download_url(
   file_path: str = Query(..., example="2024/12/27/123.txt"),
) -> DownloadLinkSchemaOut:
   """Generate presigned url for file download from S3 storage."""
   s3_service: S3Service = S3Service()
   try:
       download_link: str = s3_service.generate_download_url(file_path)
   except S3ObjectDoesntExistException:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
   return DownloadLinkSchemaOut(download_link=download_link)
