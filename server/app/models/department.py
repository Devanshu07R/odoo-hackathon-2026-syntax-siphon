from sqlalchemy import Column, String, ForeignKey

from app.database.base import Base


class Department(Base):
    name = Column(String(100), unique=True, nullable=False)

    parent_department_id = Column(
        ForeignKey("departments.id"),
        nullable=True,
    )

    status = Column(String(20), default="Active")