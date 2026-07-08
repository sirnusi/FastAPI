from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLALCHEMY_DATABASE_URL = "postgresql://todoapp_0ndo_user:qlR9jm6qxqJff9xblFYKymuiyyOo7vRV@dpg-d970icvaqgkc73cmkiq0-a.frankfurt-postgres.render.com/todoapp_0ndo"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()