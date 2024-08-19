# from typing import Annotated
# import boto3
# import logging
# import uuid
# from botocore.exceptions import ClientError
# from fastapi import APIRouter, Depends, HTTPException, UploadFile, status

# from sqlalchemy.orm import Session

# from app.database import get_db

# from .. import crud, models
# from app import oauth2, schemas


# router = APIRouter(prefix="/file", tags=["file"])


# client = boto3.client(
#     "s3",
#     aws_access_key_id="AKIAXDFC5X3NY5XT3CGH",
#     aws_secret_access_key="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",
# )

# bucket = "ewootz-s3-bucket"


# @router.post("/upload", status_code=status.HTTP_200_OK)
# async def upload(
#     file: UploadFile,
#     current_user: Annotated[schemas.UserGet, Depends(oauth2.get_authenticated_user)],
#     db: Session = Depends(get_db),
# ):
#     filename = f"{str(uuid.uuid4())}.jpg"
#     s3_key = f"/{filename}"

#     try:
#         client.upload_fileobj(file.file, bucket, s3_key)
#     except ClientError as e:
#         raise HTTPException(status_code=500, detail=f"S3 upload fails: {str(e)}")

#     url = "https://%s.s3.ap-northeast-2.amazonaws.com/%s" % (
#         bucket,
#         s3_key,
#     )

#     new_user = schemas.UserEdit(
#         profile_image=url,
#     )

#     crud.update_user(db, new_user, current_user)

#     return url


# @router.get("/download", status_code=status.HTTP_200_OK)
# def download_file(
#     current_user: Annotated[schemas.UserAuth, Depends(oauth2.get_authenticated_user)],
#     db: Session = Depends(get_db),
# ):
#     user_info = crud.get_user_by_username(db, username=current_user.username)

#     profile_image = user_info.profile_image

#     return profile_image