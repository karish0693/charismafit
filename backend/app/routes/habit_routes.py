from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import DailyHabitLog, User
from app.schemas import DailyHabitLogCreate, DailyHabitLogResponse
from app.auth import get_current_user

router = APIRouter(prefix="/habits", tags=["Habits"])


@router.post("/", response_model=DailyHabitLogResponse)
def create_habit_log(
    habit_data: DailyHabitLogCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    habit_log = DailyHabitLog(
        user_id=current_user.id,
        **habit_data.model_dump()
    )

    db.add(habit_log)
    db.commit()
    db.refresh(habit_log)

    return habit_log


@router.get("/", response_model=list[DailyHabitLogResponse])
def get_habit_logs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    logs = db.query(DailyHabitLog).filter(
        DailyHabitLog.user_id == current_user.id
    ).all()

    return logs