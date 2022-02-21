import motor.motor_asyncio
from bson.objectid import ObjectId

from app.config import get_config


config = get_config()
client = motor.motor_asyncio.AsyncIOMotorClient(config.mongo_db_path)

database = client.files
file_collection = database.get_collection("file_collection")
# student_collection = database.get_collection("students_collection")

# helper


# def student_helper(student) -> dict:
#     return {
#         "id": str(student["_id"]),
#         "fullname": student["fullname"],
#         "email": student["email"],
#         "course_of_study": student["course_of_study"],
#         "year": student["year"],
#         "GPA": student["gpa"],
#     }


def file_helper(file) -> dict:
    return {
        "id": str(file["_id"]),
        "name": file["name"],
        "path": file["path"],
        "hash": file["hash"],
        "column_attributes": file["column_attributes"],
        "description": file["description"],
        "type": file["type"],
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

# async def retrive_student(id: str) -> dict:
#     if student := await student_collection.find_one({"_id": ObjectId(id)}):
#         return student_helper(student)


# async def update_student(id: str, data: dict):
#     if len(data) < 1:
#         return False
#     if student := await student_collection.find_one({"_id": ObjectId(id)}):
#         if updated_student := await student_collection.update_one({"_id": ObjectId(id)}, {"$set": data}):
#             return True
#         return False


# async def delete_student(id: str):
#     if student := await student_collection.find_one({"_id": ObjectId(id)}):
#         await student_collection.delete_one({"_id": ObjectId(id)})
#         return True
    