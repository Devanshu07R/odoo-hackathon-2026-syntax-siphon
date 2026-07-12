from sqlalchemy import Column, String, ForeignKey

from app.database.base import Base


class User(Base):
    first_name = Column(String(50), nullable=False)

    last_name = Column(String(50), nullable=False)

    email = Column(String(255), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    phone = Column(String(20), nullable=True)

    role_id = Column(
        ForeignKey("roles.id"),
        nullable=False,
    )

    department_id = Column(
        ForeignKey("departments.id"),
        nullable=True,
    )

    status = Column(String(20), default="Active")