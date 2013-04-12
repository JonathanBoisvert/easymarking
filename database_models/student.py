import database
from sqlalchemy import Column, Table, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from database_models.course import Course
from database_models.handed_assignment import HandedAssignment

enrolled = Table(
    'enrolled', 
    database.Base.metadata,
    Column('student_id', String(20), ForeignKey('students.student_id')),
    Column('course_id', String(20), ForeignKey('courses.course_id'))
)

class Student(database.Base):
    __tablename__ = 'students'

    student_id = Column(String(20), primary_key=True)
    email = Column(String(254)) #TODO: figure out if this value is nullable
    courses = relationship(
        "Course",
        secondary=enrolled,
        backref="students"
    )    
    handed_assignments = relationship("HandedAssignment")

    def __init__(self, student_id, email=None):
        self.student_id = student_id
        self.email = email

    def __repr__(self):
        return '<Student student_id=%r email=%r>' % (
            self.student_id,
            self.email
        )      

    @classmethod
    def get(cls, student_id):
        return cls.query.filter_by(student_id=student_id).first()

    @classmethod
    def contains(cls, student_id):
        contains = False
        if cls.query.filter_by(student_id=student_id).first() is not None:
            contains = True
        return contains

    @classmethod
    def is_enrolled(cls, student_id, course_id):
        student = cls.get(student_id)
        course = Course.get(course_id)
        return course in student.courses

    @classmethod
    def enroll(cls, student_id, course_id):
        student = cls.get(student_id)
        course = Course.get(course_id)
        student.courses.append(course)

    @classmethod
    def has_handed_assignment_for_course(cls, student_id, course_id, assignment_number):
        student = cls.get(student_id)
        handed_assignment = HandedAssignment.get(
            student_id,
            course_id, 
            assignment_number
        )
        return handed_assignment in student.handed_assignments

    @classmethod
    def create_handed_assignment(cls, student_id, course_id, assignment_number):
        student = cls.get(student_id)
        handed_assignment = HandedAssignment(
            student_id,
            course_id, 
            assignment_number
        )     
        student.handed_assignments.append(handed_assignment)  

