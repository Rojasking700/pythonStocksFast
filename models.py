from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


##############################################
#### Run Database Migrations (Alembic)###
###Initialize Alembic:###

# alembic init alembic

###Edit alembic.ini to match the DATABASE_URL.###
###Then, create and apply migrations:###

# alembic revision --autogenerate -m "create users table"
# alembic upgrade head