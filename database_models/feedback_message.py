import database
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

class FeedbackMessage(database.Base):
    """ Stores custom feedback message that can be appended
        to handed assignments.
    """
    __tablename__ = 'feedback_messages'

    id = Column(Integer, primary_key=True)
    message = Column(String(500), nullable=False)
    marks_to_deduct = Column(Float)
    aliases = relationship("FBMessageAlias")

    def __init__(self, alias, message, marks_to_deduct):
        self.aliases.append(alias)
        self.message = message
        self.marks_to_deduct = marks_to_deduct

    def __repr__(self):
        return '<FeedbackMessage %r %r>' % (
            self.message,
            self.marks_to_deduct
        )      

class FBMessageAlias(database.Base):
    """ Represents a table containing the aliases feedback
        messages.
    """    
    __tablename__ = 'fb_message_aliases'

    alias = Column(String(50), primary_key=True)
    message_id = Column(
        Integer,
        ForeignKey('feedback_messages.id', ondelete='CASCADE')
    )

    def __init__(self, alias):
        self.alias = alias

    def __repr__(self):
        return '<FBMessageAlias message_id=%r, alias=%r>' % (
            self.message_id,
            self.alias
        )   