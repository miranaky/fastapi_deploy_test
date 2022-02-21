import motor.motor_asyncio
from bson.objectid import ObjectId

from app.config import get_config


config = get_config()
client = motor.motor_asyncio.AsyncIOMotorClient(config.mongo_db_path)

database = client.students

student_collection = database.get_collection("students_collection")

# helper


def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }


async def retrive_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students


async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


async def retrive_student(id: str) -> dict:
    if student := await student_collection.find_one({"_id": ObjectId(id)}):
        return student_helper(student)


async def update_student(id: str, data: dict):
    if len(data) < 1:
        return False
    if student := await student_collection.find_one({"_id": ObjectId(id)}):
        if updated_student := await student_collection.update_one({"_id": ObjectId(id)}, {"$set": data}):
            return True
        return False


async def delete_student(id: str):
    if student := await student_collection.find_one({"_id": ObjectId(id)}):
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True
    