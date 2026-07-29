def calculate_capacity_score(
    available_hours_per_week: float,
    stress_level: str,
    energy_level: int,
    motivation_level: int,
    confidence_level: int,
    previous_attempts: str
) -> int:
    score = 100

    # Time availability
    if available_hours_per_week < 2:
        score -= 20
    elif available_hours_per_week < 4:
        score -= 10

    # Stress level
    stress = stress_level.lower()

    if stress == "very high":
        score -= 25
    elif stress == "high":
        score -= 15
    elif stress == "moderate":
        score -= 8

    # Energy level
    if energy_level <= 3:
        score -= 20
    elif energy_level <= 5:
        score -= 10

    # Motivation level
    if motivation_level <= 3:
        score -= 15
    elif motivation_level <= 5:
        score -= 8

    # Confidence level
    if confidence_level <= 3:
        score -= 20
    elif confidence_level <= 5:
        score -= 10

    # Previous attempts
    attempts = previous_attempts.lower()

    if attempts == "more_than_5":
        score -= 10
    elif attempts == "3-5":
        score -= 5

    return max(0, min(score, 100))


def get_capacity_stage(score: int) -> str:
    if score <= 40:
        return "Foundation"
    elif score <= 60:
        return "Building"
    elif score <= 80:
        return "Growth"
    else:
        return "Optimization"