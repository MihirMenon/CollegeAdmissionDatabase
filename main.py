from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from models import *
from database import query_all, insert_record

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/home", response_class=FileResponse)
def serve_index():
    return "static/index.html"

@app.get("/", response_class=FileResponse)
def serve_login():
    return "static/login.html"

# GET + POST per table

@app.get("/students")
def get_students():
    return query_all("Student")

@app.post("/students")
def add_student(student: Student):
    insert_record("Student", list(student.dict().keys()), tuple(student.dict().values()))
    return {"message": "Student added"}

@app.get("/courses")
def get_courses():
    return query_all("Course")

@app.post("/courses")
def add_course(course: Course):
    insert_record("Course", list(course.dict().keys()), tuple(course.dict().values()))
    return {"message": "Course added"}

@app.get("/departments")
def get_departments():
    return query_all("Department")

@app.post("/departments")
def add_department(dept: Department):
    insert_record("Department", list(dept.dict().keys()), tuple(dept.dict().values()))
    return {"message": "Department added"}

@app.get("/programs")
def get_programs():
    return query_all("Program")

@app.post("/programs")
def add_program(program: Program):
    insert_record("Program", list(program.dict().keys()), tuple(program.dict().values()))
    return {"message": "Program added"}

@app.get("/applications")
def get_applications():
    return query_all("Application")

@app.post("/applications")
def add_application(apply: Application):
    insert_record("Application", list(apply.dict().keys()), tuple(apply.dict().values()))
    return {"message": "Application added"}

@app.get("/admissions")
def get_admissions():
    return query_all("Admission")

@app.post("/admissions")
def add_admission(adm: Admission):
    insert_record("Admission", list(adm.dict().keys()), tuple(adm.dict().values()))
    return {"message": "Admission added"}

@app.get("/entrance-exams")
def get_entrance_exams():
    return query_all("EntranceExam")

@app.post("/entrance-exams")
def add_exam(exam: EntranceExam):
    insert_record("EntranceExam", list(exam.dict().keys()), tuple(exam.dict().values()))
    return {"message": "Exam added"}

@app.get("/exam-results")
def get_exam_results():
    return query_all("ExamResult")

@app.post("/exam-results")
def add_result(result: ExamResult):
    insert_record("ExamResult", list(result.dict().keys()), tuple(result.dict().values()))
    return {"message": "Result added"}

@app.get("/fee-structures")
def get_fee_structures():
    return query_all("FeeStructure")

@app.post("/fee-structures")
def add_fee(fee: FeeStructure):
    insert_record("FeeStructure", list(fee.dict().keys()), tuple(fee.dict().values()))
    return {"message": "Fee record added"}

@app.get("/payments")
def get_payments():
    return query_all("Payment")

@app.post("/payments")
def add_payment(payment: Payment):
    insert_record("Payment", list(payment.dict().keys()), tuple(payment.dict().values()))
    return {"message": "Payment added"}

@app.get("/documents")
def get_documents():
    return query_all("Document")

@app.post("/documents")
def add_document(doc: Document):
    insert_record("Document", list(doc.dict().keys()), tuple(doc.dict().values()))
    return {"message": "Document added"}

@app.get("/scholarships")
def get_scholarships():
    return query_all("Scholarship")

@app.post("/scholarships")
def add_scholarship(sch: Scholarship):
    insert_record("Scholarship", list(sch.dict().keys()), tuple(sch.dict().values()))
    return {"message": "Scholarship added"}

@app.get("/faculties")
def get_faculties():
    return query_all("Faculty")

@app.post("/faculties")
def add_faculty(fac: Faculty):
    insert_record("Faculty", list(fac.dict().keys()), tuple(fac.dict().values()))
    return {"message": "Faculty added"}

@app.get("/notifications")
def get_notifications():
    return query_all("Notification")

@app.post("/notifications")
def add_notification(notif: Notification):
    insert_record("Notification", list(notif.dict().keys()), tuple(notif.dict().values()))
    return {"message": "Notification added"}

@app.get("/interviews")
def get_interviews():
    return query_all("Interview")

@app.post("/interviews")
def add_interview(intv: Interview):
    insert_record("Interview", list(intv.dict().keys()), tuple(intv.dict().values()))
    return {"message": "Interview added"}
