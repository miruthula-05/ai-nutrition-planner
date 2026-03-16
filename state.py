from __future__ import annotations

import streamlit as st


DEFAULT_STATE = {
    "db_ready": False,
    "db_error": "",
    "is_authenticated": False,
    "current_user_id": None,
    "profile_saved": False,
    "profile": {"name": "", "email": "", "phone": ""},
    "body": {
        "gender": "Male",
        "height": 170.0,
        "weight": 70.0,
        "goal": "Maintain",
    },
    "exercise_count": 2,
    "exercises": [],
    "exercise_summary": [],
    "total_burn": 0,
    "total_calories": 0,
    "protein": 0,
    "carbs": 0,
    "fats": 0,
    "meal_split": {},
    "suggested_meals": {},
    "selected_meals": {},
    "current_page": 0,
}


def init_state() -> None:
    for key, value in DEFAULT_STATE.items():
        if key not in st.session_state:
            st.session_state[key] = value
