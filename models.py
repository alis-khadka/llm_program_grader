from sqlalchemy import Column, String, Text, Enum, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import declarative_base, relationship
import enum

Base = declarative_base()

class DeepSeekModel(enum.Enum):
    MODEL_32B = "DeepSeek-R1-Distill-Qwen-32B"
    MODEL_1_5B = "DeepSeek-R1-Distill-Qwen-1.5B"

class Question(Base):
    __tablename__ = 'questions'

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Question(id={self.id}, title={self.title}, description={self.description}, created={self.created_at})>"

class StudentSubmission(Base):
    __tablename__ = 'student_submissions'

    id = Column(String, primary_key=True)
    student_code = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    grades = relationship("Grade", back_populates="submission")

    def __repr__(self):
        return f"<StudentSubmission(id={self.id}, student_code={self.student_code}, created_at={self.created_at})>"

class Grade(Base):
    __tablename__ = 'grades'

    deepseek_model = Column(Enum(DeepSeekModel), primary_key=True)
    student_id = Column(String, ForeignKey('student_submissions.id'), primary_key=True)

    analysis_functionality = Column(Text, nullable=False)
    analysis_functionality_json = Column(Text, nullable=False)

    analysis_code_quality = Column(Text, nullable=False)
    analysis_code_quality_json = Column(Text, nullable=False)

    analysis_algorithmic_efficiency = Column(Text, nullable=False)
    analysis_algorithmic_efficiency_json = Column(Text, nullable=False)

    grade = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    submission = relationship("StudentSubmission", back_populates="grades")

    def __repr__(self):
        return f"<Grade(student_id={self.student_id}, model={self.deepseek_model}, grade={self.grade}, analysis_functionality={self.analysis_functionality}, analysis_functionality_json={self.analysis_functionality_json}, analysis_code_quality={self.analysis_code_quality}, analysis_code_quality_json={self.analysis_code_quality_json}, analysis_algorithmic_efficiency={self.analysis_algorithmic_efficiency}, analysis_algorithmic_efficiency_json={self.analysis_algorithmic_efficiency_json}, created_at={self.created_at})>"
