from __future__ import annotations


EXERCISE_LIBRARY = {
    "Strength": {
        "Push-Ups": 0.42,
        "Squats": 0.36,
        "Lunges": 0.34,
        "Bench Press": 0.40,
        "Deadlifts": 0.48,
    },
    "Cardio": {
        "Jump Rope": 0.52,
        "High Knees": 0.38,
        "Mountain Climbers": 0.33,
        "Step-Ups": 0.28,
        "Jumping Jacks": 0.24,
    },
    "HIIT": {
        "Burpees": 0.60,
        "Jump Squats": 0.46,
        "Mountain Climbers": 0.36,
        "Skaters": 0.30,
        "Thrusters": 0.54,
    },
    "Rest Day": {
        "Light Stretching": 0.05,
        "Mobility Flow": 0.06,
        "Easy Walk Steps": 0.04,
    },
}


def estimate_base_calories(weight: float, gender: str) -> int:
    calories_per_kg = 24 if gender == "Female" else 26
    return int(weight * calories_per_kg)


def workout_bonus(workout_type: str) -> int:
    bonuses = {
        "Strength": 130,
        "Cardio": 160,
        "HIIT": 210,
        "Rest Day": 0,
    }
    return bonuses.get(workout_type, 0)


def goal_adjustment(goal: str) -> int:
    adjustments = {
        "Weight Loss": -320,
        "Muscle Gain": 260,
        "Maintain": 0,
    }
    return adjustments.get(goal, 0)


def estimate_calories_burned(
    workout_type: str,
    exercise_name: str,
    sets_count: int,
    reps_count: int,
    weight: float,
) -> int:
    calories_per_rep = EXERCISE_LIBRARY.get(workout_type, {}).get(exercise_name, 0.15)
    total_reps = sets_count * reps_count
    weight_factor = max(weight / 70, 0.7)
    return round(total_reps * calories_per_rep * weight_factor)


def calculate_macros(weight: float, calories: int, goal: str) -> tuple[int, int, int]:
    protein_per_kg = {
        "Weight Loss": 2.0,
        "Muscle Gain": 2.2,
        "Maintain": 1.8,
    }
    protein_grams = round(weight * protein_per_kg.get(goal, 1.8))
    fat_grams = round((calories * 0.25) / 9)
    remaining_calories = max(calories - (protein_grams * 4) - (fat_grams * 9), 0)
    carb_grams = round(remaining_calories / 4)
    return protein_grams, carb_grams, fat_grams


def build_meal_split(total_calories: int, protein: int, carbs: int, fats: int) -> dict[str, dict[str, int]]:
    return {
        "Breakfast": {
            "calories": round(total_calories / 3),
            "protein": round(protein / 3),
            "carbs": round(carbs / 3),
            "fats": round(fats / 3),
        },
        "Lunch": {
            "calories": round(total_calories / 3),
            "protein": round(protein / 3),
            "carbs": round(carbs / 3),
            "fats": round(fats / 3),
        },
        "Dinner": {
            "calories": total_calories - (round(total_calories / 3) * 2),
            "protein": protein - (round(protein / 3) * 2),
            "carbs": carbs - (round(carbs / 3) * 2),
            "fats": fats - (round(fats / 3) * 2),
        },
    }


def calculate_plan(body: dict[str, object], exercises: list[dict[str, object]]) -> dict[str, object]:
    weight = float(body["weight"])

    summaries: list[dict[str, object]] = []
    total_burn = 0
    for exercise in exercises:
        burned = estimate_calories_burned(
            workout_type=str(exercise["workout_type"]),
            exercise_name=str(exercise["exercise_name"]),
            sets_count=int(exercise["sets_count"]),
            reps_count=int(exercise["reps_count"]),
            weight=weight,
        )
        total_reps = int(exercise["sets_count"]) * int(exercise["reps_count"])
        summaries.append(
            {
                "workout_type": str(exercise["workout_type"]),
                "exercise_name": str(exercise["exercise_name"]),
                "sets_count": int(exercise["sets_count"]),
                "reps_count": int(exercise["reps_count"]),
                "total_reps": total_reps,
                "estimated_burn": burned,
            }
        )
        total_burn += burned

    primary_workout_type = str(exercises[0]["workout_type"]) if exercises else "Rest Day"
    base_calories = estimate_base_calories(weight, str(body["gender"]))
    height_adjustment = int((float(body["height"]) - 170) * 2)
    total_calories = (
        base_calories
        + height_adjustment
        + workout_bonus(primary_workout_type)
        + int(total_burn * 0.7)
        + goal_adjustment(str(body["goal"]))
    )
    total_calories = max(total_calories, 1200)

    protein, carbs, fats = calculate_macros(weight, total_calories, str(body["goal"]))

    return {
        "exercise_summary": summaries,
        "total_burn": total_burn,
        "total_calories": total_calories,
        "protein": protein,
        "carbs": carbs,
        "fats": fats,
        "meal_split": build_meal_split(total_calories, protein, carbs, fats),
        "primary_workout_type": primary_workout_type,
    }
