from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    ID: int
    Name: str
    DOB: str
    Address: Optional[str]

class Course(BaseModel):
    CourseID: int
    Name: str
    Duration: int
    Credits: int

class Department(BaseModel):
    DepartmentID: int
    Name: str
    HOD: Optional[str]

class Program(BaseModel):
    ProgramID: int
    Degree: str
    Eligibility: Optional[str]

class Application(BaseModel):
    ApplicationID: int
    SubmissionDate: str
    Status: str

class Admission(BaseModel):
    AdmissionID: int
    StudentID: int
    CourseID: int
    AdmissionDate: str

class EntranceExam(BaseModel):
    ExamDate: str
    Name: str
    ExamSlot: str

class ExamResult(BaseModel):
    StudentID: int
    Score: int
    StudentRank: int

class FeeStructure(BaseModel):
    FeeID: int
    StudentID: int
    Amount: float
    Date: str

class Payment(BaseModel):
    PaymentReferenceNumber: int
    StudentID: int
    Amount: float
    Method: str

class Document(BaseModel):
    DocumentType: str
    Description: str
    StudentID: int

class Scholarship(BaseModel):
    ScholarshipID: int
    ScholarshipName: str
    Amount: float

class Faculty(BaseModel):
    FacultyID: int
    Name: str
    DepartmentID: int
    Designation: str

class Notification(BaseModel):
    NotificationID: int
    Title: str
    Description: Optional[str]
    Date: str

class Interview(BaseModel):
    InterviewID: int
    ApplicationID: int
    Date: str
    Mode: str
