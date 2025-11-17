from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app import schemas, crud

router = APIRouter()


@router.get("/questions/", response_model=List[schemas.QuestionResponse])
def read_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    questions = crud.get_questions(db, skip=skip, limit=limit)
    return questions


@router.post("/questions/", response_model=schemas.QuestionResponse)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    if not question.text.strip():
        raise HTTPException(status_code=400, detail="Текст вопроса не может быть пустым")
    return crud.create_question(db=db, question=question)


@router.get("/questions/{question_id}", response_model=schemas.QuestionWithAnswers)
def read_question(question_id: int, db: Session = Depends(get_db)):
    db_question = crud.get_question(db, question_id=question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")

    answers = crud.get_answers_by_question(db, question_id=question_id)
    question_data = schemas.QuestionWithAnswers(
        id=db_question.id,
        text=db_question.text,
        created_at=db_question.created_at,
        answers=answers
    )
    return question_data


@router.delete("/questions/{question_id}")
def delete_question(question_id: int, db: Session = Depends(get_db)):
    success = crud.delete_question(db, question_id=question_id)
    if not success:
        raise HTTPException(status_code=404, detail="Question not found")
    return {"message": "Question deleted"}


@router.post("/questions/{question_id}/answers/", response_model=schemas.AnswerResponse)
def create_answer(question_id: int, answer: schemas.AnswerCreate, db: Session = Depends(get_db)):
    question = crud.get_question(db, question_id=question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    if not answer.text.strip():
        raise HTTPException(status_code=400, detail="Текст ответа не может быть пустым")

    if not answer.user_id.strip():
        raise HTTPException(status_code=400, detail="User ID не может быть пустым")

    return crud.create_answer(db=db, answer=answer, question_id=question_id)


@router.get("/answers/{answer_id}", response_model=schemas.AnswerResponse)
def read_answer(answer_id: int, db: Session = Depends(get_db)):
    db_answer = crud.get_answer(db, answer_id=answer_id)
    if db_answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")
    return db_answer


@router.delete("/answers/{answer_id}")
def delete_answer(answer_id: int, db: Session = Depends(get_db)):
    success = crud.delete_answer(db, answer_id=answer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Answer not found")
    return {"message": "Answer deleted"}