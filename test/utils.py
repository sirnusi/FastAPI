from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool

from routers.auth import bcrypt_context
from models import Todos, Users

from database import Base
import pytest
from main import app

from sqlalchemy.orm import sessionmaker


SQLACHEMY_DATABASE_URL = "sqlite:///./testdb.db"
engine = create_engine(SQLACHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False},
                       poolclass=StaticPool,)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {'username': 'nusimoney', 'id':1, 'user_role': 'admin'}

client = TestClient(app)

@pytest.fixture
def test_todo():
    todo = Todos(title="Django is good",
                 description='The best yet to come!',
                 priority=3,
                 complete=False,
                 owner_id=1)
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()


@pytest.fixture
def test_user():
    user = Users(
        username='nusimoney',
        email='nusi1234@gmail.com',
        first_name="Nusi",
        last_name="Sanusi",
        hashed_password=bcrypt_context.hash("testpassword"),
        role="admin",
        phone_number="(111)-111-111"
    )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()
    