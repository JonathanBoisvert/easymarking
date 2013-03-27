from sqlalchemy import Column, ForeignKey, Integer
import database

class Feedback(database.Base):
    __tablename__ = 'feedback'

    student_id = Column(
    	Integer, 
    	primary_key=True,
    	ForeignKey("students.id")
    )
    message_id = Column(
    	Integer, 
    	primary_key=True,
    	ForeignKey("feedback_message.id")
    )

    def __init__(self, student_id, message_id):
        self.student_id = student_id
        self.message_id = message_id

    def __repr__(self):
        return '<Feedback %r>' % (
            self.school_id,
            self.message_id
        )      
