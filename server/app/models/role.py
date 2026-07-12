from sqlalchemy import Column, String

from app.database.base import Base


class Role(Base):
    name = Column(String(50), unique=True, nullable=False)

    description = Column(String(255), nullable=True)