import motor.motor_asyncio
from bson.objectid import ObjectId

from app.config import get_config


config = get_config()
client = motor.motor_asyncio.AsyncIOMotorClient(config.mongo_db_path)

database = client.files
file_collection = database.get_collection("file_collection")


def file_helper(file) -> dict:
    return {
        "id": str(file["_id"]),
        "name": file["name"],
        "path": file["path"],
        "hash": file["hash"],
    }


async def add_file(data: dict) -> dict:
    file = await file_collection.insert_one(data)
    new_file = await file_collection.find_one({"_id": file.inserted_id})
    return file_helper(new_file)


async def get_file_from_hash(hash: str) -> dict:
    if file := await file_collection.find_one({"hash": hash}):
        return file_helper(file)


async def get_file_from_id(id: str) -> dict:
    if file := await file_collection.find_one({"_id": ObjectId(id)}):
        return file_helper(file)


async def update_file(id: str, data: dict) -> dict:
    if len(data) < 1:
        return False
    if file := await file_collection.find_one({"_id": ObjectId(id)}):
        if update_file := await file_collection.update_one({"_id": ObjectId(id)}, {"$set": data}):
            return file_helper(update_file)
    return False
