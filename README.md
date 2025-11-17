# QA Service API

API-сервис для вопросов и ответов, построенный на FastAPI и PostgreSQL.

## Функциональность

- Создание, получение и удаление вопросов
- Добавление ответов к вопросам
- Получение и удаление ответов
- Валидация данных
- Каскадное удаление ответов при удалении вопроса

## Технологии

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Docker & docker compose
- Pytest

## Запуск проекта

### Требования
- Docker
- Docker Compose


### 1. Клонирование и запуск
```bash
# Клонируй репозиторий
git clone <repository-url>
cd qa_service

# Запусти проект
docker-compose up --build