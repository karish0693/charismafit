from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.database import Base
from sqlalchemy import Float, ForeignKey, Text
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class FitnessProfile(Base):
    __tablename__ = "fitness_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    age = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)
    height_cm = Column(Float, nullable=True)
    weight_kg = Column(Float, nullable=True)

    goals = Column(Text, nullable=True)
    activity_level = Column(String, nullable=True)

    sleep_hours = Column(Float, nullable=True)
    water_liters_per_day = Column(Float, nullable=True)
    stress_level = Column(String, nullable=True)
    daily_steps = Column(Integer, nullable=True)

    health_conditions = Column(Text, nullable=True)
    injuries = Column(Text, nullable=True)

    favorite_foods = Column(Text, nullable=True)
    non_negotiable_foods = Column(Text, nullable=True)
    main_barriers = Column(Text, nullable=True)

    motivation_style = Column(String, nullable=True)
    strictness_level = Column(String, nullable=True)
    preferred_workout_type = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User")

class DailyHabitLog(Base):
    __tablename__ = "daily_habit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    sleep_hours = Column(Float, nullable=True)
    water_liters = Column(Float, nullable=True)
    steps = Column(Integer, nullable=True)

    read_nonfiction_pages = Column(Integer, nullable=True)
    screen_time_hours = Column(Float, nullable=True)

    movement_breaks = Column(Integer, nullable=True)
    standing_breaks = Column(Integer, nullable=True)

    balanced_food = Column(String, nullable=True)

    notes = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User")

class ReadinessAssessment(Base):
    __tablename__ = "readiness_assessments"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    available_hours_per_week = Column(Float)

    stress_level = Column(String)
    energy_level = Column(Integer)

    motivation_level = Column(Integer)
    confidence_level = Column(Integer)

    fitness_experience = Column(String)

    biggest_challenges = Column(Text)

    previous_attempts = Column(String)

    capacity_score = Column(Integer)

    stage = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user = relationship("User")