from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str

class ProfileCreate(BaseModel):
    age: Optional[int] = None
    gender: Optional[str] = None
    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None

    goals: Optional[str] = None
    activity_level: Optional[str] = None

    sleep_hours: Optional[float] = None
    water_liters_per_day: Optional[float] = None
    stress_level: Optional[str] = None
    daily_steps: Optional[int] = None

    health_conditions: Optional[str] = None
    injuries: Optional[str] = None

    favorite_foods: Optional[str] = None
    non_negotiable_foods: Optional[str] = None
    main_barriers: Optional[str] = None

    motivation_style: Optional[str] = None
    strictness_level: Optional[str] = None
    preferred_workout_type: Optional[str] = None


class ProfileResponse(ProfileCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True

class DailyHabitLogCreate(BaseModel):
    sleep_hours: Optional[float] = None
    water_liters: Optional[float] = None
    steps: Optional[int] = None

    read_nonfiction_pages: Optional[int] = None
    screen_time_hours: Optional[float] = None

    movement_breaks: Optional[int] = None
    standing_breaks: Optional[int] = None

    balanced_food: Optional[str] = None
    notes: Optional[str] = None


class DailyHabitLogResponse(DailyHabitLogCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True

class AssessmentCreate(BaseModel):
    available_hours_per_week: float

    stress_level: str
    energy_level: int

    motivation_level: int
    confidence_level: int

    fitness_experience: str

    biggest_challenges: str

    previous_attempts: str

class AssessmentResponse(AssessmentCreate):
    id: int
    capacity_score: int
    stage: str

    class Config:
        from_attributes = True