from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.db import add_student, delete_student, retrive_student, retrive_students, update_student
from app.models import ErrorResponseModel, ResponseModel, StudentSchema, UpdateStudentModel

router = APIRouter()


@router.post("/", response_description="Create new student data at the database")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Student add successfully.")


@router.get("/", response_description="Get all students data from the database")
async def get_students():
    students = await retrive_students()
    if students:
        return ResponseModel(students, "Students data retrived")
    return ResponseModel(students, "Empty list returned")


@router.get("/{id}", response_description="Student data retrived")
async def get_student_data(id: str):
    student = await retrive_student(id)
    if student:
        return ResponseModel(student, "Student data retrived")
    return ErrorResponseModel("An error occured", 404, f"Student {id} doesn't exist.")


@router.put("/{id}")
async def update_student_data(id: str, req: UpdateStudentModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_student(id, req)
    if updated_student:
        return ResponseModel(f"Student with ID: {id} name update is successful.", f"Student {id} updated successfully")
    return ErrorResponseModel("An Error Occured", 404, f"Student {id} doesn't exists.")


@router.delete("/{id}", response_description="Student data delete from the database")
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    if deleted_student:
        return ResponseModel(f"Student ID: {id} removed.", "Student deleted successfully")
    return ErrorResponseModel("Student {id} doesn't exist", 404, "Student {id} doesn't exist")
