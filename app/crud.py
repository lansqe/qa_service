from sqlalchemy.orm import Session
from app import models, schemas

def get_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Question).offset(skip).limit(limit).all()

def get_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()

def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(text=question.text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def delete_question(db: Session, question_id: int):
    question = get_question(db, question_id)
    if question:
        db.delete(question)
        db.commit()
        return True
    return False

def get_answers_by_question(db: Session, question_id: int):
    return db.query(models.Answer).filter(models.Answer.question_id == question_id).all()

def get_answer(db: Session, answer_id: int):
    return db.query(models.Answer).filter(models.Answer.id == answer_id).first()

def create_answer(db: Session, answer: schemas.AnswerCreate, question_id: int):
    db_answer = models.Answer(
        text=answer.text,
        user_id=answer.user_id,
        question_id=question_id
    )
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

def delete_answer(db: Session, answer_id: int):
    answer = get_answer(db, answer_id)
    if answer:
        db.delete(answer)
        db.commit()
        return True
    return False