import os
from fastapi import APIRouter, File, UploadFile
import pandas as pd

from app.db import add_file, get_file_from_hash, get_file_from_id
from app.models import ErrorResponseModel, ResponseModel
from app.utils import get_sha256_hash

router = APIRouter()


@router.post("/")
async def upload_file(file: UploadFile):
    UPLOAD_DIRECTORY = "/data/"
    contents = await file.read()
    tmp_path = os.path.join(UPLOAD_DIRECTORY, file.filename + ".tmp")

    # check same file exist.
    with open(tmp_path, "wb") as tmp_f:
        tmp_f.write(contents)
    tmp_hash = get_sha256_hash(tmp_path)
    if exist_file := await get_file_from_hash(tmp_hash):
        return ResponseModel(exist_file, "file already exist")

    # write file
    dir_path = os.path.join(UPLOAD_DIRECTORY, tmp_hash)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = os.path.join(dir_path, file.filename)
    os.rename(tmp_path, file_path)
    new_file = await add_file({"name": file.filename, "path": file_path, "hash": tmp_hash})
    return ResponseModel(new_file, "new file add successfully.")
