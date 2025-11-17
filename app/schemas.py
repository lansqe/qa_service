from pydantic import BaseModel
from datetime import datetime
from typing import List


class QuestionBase(BaseModel):
    text: str


class QuestionCreate(QuestionBase):
    pass


class QuestionResponse(QuestionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class AnswerBase(BaseModel):
    text: str
    user_id: str


class AnswerCreate(AnswerBase):
    pass


class AnswerResponse(AnswerBase):
    id: int
    question_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class QuestionWithAnswers(QuestionResponse):
    answers: List[AnswerResponse] = []