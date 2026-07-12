from sqlalchemy.orm import Session

from app.crud.user import (
    get_user_by_email,
    create_user,
)

from app.models.user import User
from app.core.security import hash_password


def register_user(
    db: Session,
    first_name: str,
    last_name: str,
    email: str,
    password: str,
    department_id: int,
    phone: str = None,
    role_id: int = 1,
):
    existing = get_user_by_email(db, email)

    if existing:
        return None

    user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password_hash=hash_password(password),
        phone=phone,
        department_id=department_id,
        role_id=role_id,
        status="Active",
    )

    return create_user(db, user)