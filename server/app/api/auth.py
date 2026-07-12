from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.auth import RegisterRequest
from app.schemas.user import UserResponse

from app.services.auth_service import register_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
):

    user = register_user(
        db=db,
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        password=request.password,
        phone=request.phone,
        department_id=request.department_id,
    )

    if not user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists",
        )

    return user