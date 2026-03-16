from __future__ import annotations

import streamlit as st

from auth import hash_password, verify_password
from db import create_user, get_user_by_email, init_database
from logic import EXERCISE_LIBRARY, calculate_plan
from meals import suggest_meals
from state import init_state
from theme import apply_theme


st.set_page_config(
    page_title="AI Nutrition Planner",
    layout="wide",
    initial_sidebar_state="expanded",
)


def compute_plan() -> None:
    plan = calculate_plan(st.session_state.body, st.session_state.exercises)
    st.session_state.exercise_summary = plan["exercise_summary"]
    st.session_state.total_burn = plan["total_burn"]
    st.session_state.total_calories = plan["total_calories"]
    st.session_state.protein = plan["protein"]
    st.session_state.carbs = plan["carbs"]
    st.session_state.fats = plan["fats"]
    st.session_state.meal_split = plan["meal_split"]
    st.session_state.suggested_meals = suggest_meals(
        str(st.session_state.body["goal"]),
        str(plan["primary_workout_type"]),
    )
    st.session_state.selected_meals = {}


def render_metric(label: str, value: str) -> None:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_header() -> None:
    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-title">AI Nutrition Planner</div>
            <p class="hero-copy">
                Move step by step through your profile, body details, workout log, meal suggestions,
                and recipe page. Your personal details only need to be saved once.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def go_to_page(page_number: int) -> None:
    st.session_state.current_page = page_number
    st.rerun()


def render_back_button(page_number: int) -> None:
    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
    if page_number > 0 and st.button("Back", key=f"back_{page_number}"):
        go_to_page(page_number - 1)


def render_auth_required(page_number: int) -> bool:
    if st.session_state.is_authenticated:
        return False

    st.warning("Please sign up or log in on the first page before using the planner.")
    if page_number != 0 and st.button("Go To Login"):
        go_to_page(0)
    return True


def page_profile() -> None:
    st.subheader("Login / Profile")

    if not st.session_state.db_ready:
        st.error(
            "MySQL is not connected yet. Please set `MYSQL_HOST`, `MYSQL_PORT`, `MYSQL_USER`, "
            "`MYSQL_PASSWORD`, and `MYSQL_DATABASE`, then restart the app."
        )
        if st.session_state.db_error:
            st.caption(st.session_state.db_error)
        return

    if st.session_state.is_authenticated:
        profile = st.session_state.profile
        st.success("You are logged in.")
        st.markdown(
            f"""
            <div class="panel-card">
                <div class="section-title">Account Details</div>
                <p class="soft-text">
                    Name: <strong>{profile["name"]}</strong><br>
                    Email: <strong>{profile["email"]}</strong><br>
                    Phone: <strong>{profile["phone"]}</strong>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Log Out"):
            st.session_state.is_authenticated = False
            st.session_state.current_user_id = None
            st.session_state.profile_saved = False
            st.session_state.profile = {"name": "", "email": "", "phone": ""}
            st.session_state.current_page = 0
            st.rerun()
        if st.button("Continue To Body Details"):
            go_to_page(1)
        return

    auth_mode = st.radio("Choose Access Mode", ["Sign Up", "Login"], horizontal=True)

    if auth_mode == "Sign Up":
        with st.form("signup_form"):
            st.markdown("**Full Name**")
            name = st.text_input("Full Name", label_visibility="collapsed")
            st.markdown("**Email Address**")
            email = st.text_input("Email Address", label_visibility="collapsed")
            st.markdown("**Phone Number**")
            phone = st.text_input("Phone Number", label_visibility="collapsed")
            st.markdown("**Password**")
            password = st.text_input("Password", type="password", label_visibility="collapsed")
            st.markdown("**Confirm Password**")
            confirm_password = st.text_input("Confirm Password", type="password", label_visibility="collapsed")
            save_profile = st.form_submit_button("Create Account")

        if save_profile:
            if not name.strip() or not email.strip() or not phone.strip() or not password:
                st.error("Please fill in name, email, phone number, and password.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            else:
                success, message = create_user(
                    name=name.strip(),
                    email=email.strip(),
                    phone=phone.strip(),
                    password_hash=hash_password(password),
                )
                if not success:
                    st.error(message)
                else:
                    user = get_user_by_email(email.strip())
                    if user is None:
                        st.error("Account was created, but login details could not be loaded.")
                    else:
                        st.session_state.is_authenticated = True
                        st.session_state.current_user_id = user["id"]
                        st.session_state.profile_saved = True
                        st.session_state.profile = {
                            "name": user["name"],
                            "email": user["email"],
                            "phone": user["phone"],
                        }
                        go_to_page(1)
    else:
        with st.form("login_form"):
            st.markdown("**Email Address**")
            email = st.text_input("Email Address", label_visibility="collapsed")
            st.markdown("**Password**")
            password = st.text_input("Password", type="password", label_visibility="collapsed")
            login = st.form_submit_button("Log In")

        if login:
            if not email.strip() or not password:
                st.error("Please enter your email and password.")
            else:
                user = get_user_by_email(email.strip())
                if user is None or not verify_password(password, user["password_hash"]):
                    st.error("Invalid email or password.")
                else:
                    st.session_state.is_authenticated = True
                    st.session_state.current_user_id = user["id"]
                    st.session_state.profile_saved = True
                    st.session_state.profile = {
                        "name": user["name"],
                        "email": user["email"],
                        "phone": user["phone"],
                    }
                    go_to_page(1)


def page_body_details() -> None:
    if render_auth_required(1):
        return
    st.subheader("Body Details")

    with st.form("body_form"):
        left, right = st.columns(2)
        with left:
            st.markdown("**Gender / Sex**")
            gender = st.selectbox(
                "Gender / Sex",
                ["Male", "Female"],
                index=["Male", "Female"].index(st.session_state.body["gender"]),
                label_visibility="collapsed",
            )
            st.markdown("**Your Height (cm)**")
            height = st.number_input(
                "Your Height (cm)",
                min_value=100.0,
                max_value=250.0,
                value=float(st.session_state.body["height"]),
                step=1.0,
                label_visibility="collapsed",
            )
        with right:
            st.markdown("**Your Weight (kg)**")
            weight = st.number_input(
                "Your Weight (kg)",
                min_value=30.0,
                max_value=250.0,
                value=float(st.session_state.body["weight"]),
                step=1.0,
                label_visibility="collapsed",
            )
            st.markdown("**Purpose of Training**")
            goal = st.selectbox(
                "Purpose of Training",
                ["Weight Loss", "Muscle Gain", "Maintain"],
                index=["Weight Loss", "Muscle Gain", "Maintain"].index(st.session_state.body["goal"]),
                label_visibility="collapsed",
            )

        save_body = st.form_submit_button("Save Body Details")

    if save_body:
        st.session_state.body = {
            "gender": gender,
            "height": height,
            "weight": weight,
            "goal": goal,
        }
        go_to_page(2)

    render_back_button(1)


def page_exercises() -> None:
    if render_auth_required(2):
        return
    st.subheader("Exercises Done And Calories Burnt")
    st.markdown("**Number of Exercises Done Today**")
    exercise_count = st.number_input(
        "Number of Exercises Done Today",
        min_value=1,
        max_value=10,
        value=int(st.session_state.exercise_count),
        step=1,
        help="Enter how many different exercises you completed today.",
        label_visibility="collapsed",
    )
    st.caption("Example: push-ups, squats, and jumping jacks means `3` exercises.")

    with st.form("exercise_form"):
        exercise_entries = []
        for index in range(int(exercise_count)):
            st.markdown(f"**Exercise {index + 1}**")
            col1, col2, col3, col4 = st.columns(4)

            previous = st.session_state.exercises[index] if index < len(st.session_state.exercises) else {}
            default_type = previous.get("workout_type", "Strength")

            with col1:
                workout_type = st.selectbox(
                    f"Exercise {index + 1} Type",
                    ["Strength", "Cardio", "HIIT", "Rest Day"],
                    index=["Strength", "Cardio", "HIIT", "Rest Day"].index(default_type),
                )

            exercise_names = list(EXERCISE_LIBRARY[workout_type].keys())
            default_name = previous.get("exercise_name", exercise_names[0])
            default_name_index = exercise_names.index(default_name) if default_name in exercise_names else 0

            with col2:
                exercise_name = st.selectbox(
                    f"Exercise {index + 1} Name",
                    exercise_names,
                    index=default_name_index,
                )

            with col3:
                reps = st.number_input(
                    f"Exercise {index + 1} Reps",
                    min_value=1,
                    max_value=200,
                    value=int(previous.get("reps_count", 12 if workout_type == "Strength" else 20)),
                    step=1,
                )

            with col4:
                sets = st.number_input(
                    f"Exercise {index + 1} Sets",
                    min_value=1,
                    max_value=20,
                    value=int(previous.get("sets_count", 4 if workout_type in {"Strength", "HIIT"} else 3)),
                    step=1,
                )

            exercise_entries.append(
                {
                    "workout_type": workout_type,
                    "exercise_name": exercise_name,
                    "reps_count": int(reps),
                    "sets_count": int(sets),
                }
            )

        save_exercises = st.form_submit_button("Calculate Calories Burnt")

    if save_exercises:
        st.session_state.exercise_count = int(exercise_count)
        st.session_state.exercises = exercise_entries
        compute_plan()
        go_to_page(3)

    if st.session_state.exercise_summary:
        st.markdown('<div class="section-title">Exercise Summary</div>', unsafe_allow_html=True)
        for item in st.session_state.exercise_summary:
            st.markdown(
                f"""
                <div class="panel-card">
                    <div class="section-title">{item["exercise_name"]}</div>
                    <p class="soft-text">
                        Type: <strong>{item["workout_type"]}</strong><br>
                        Sets x reps: <strong>{item["sets_count"]} x {item["reps_count"]}</strong><br>
                        Total reps: <strong>{item["total_reps"]}</strong><br>
                        Calories burnt: <strong>{item["estimated_burn"]} kcal</strong>
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            render_metric("Total Calories Burnt", f"{st.session_state.total_burn} kcal")
        with col2:
            render_metric("Daily Calories", f"{st.session_state.total_calories} kcal")
        with col3:
            render_metric("Protein", f"{st.session_state.protein} g")
        with col4:
            render_metric("Carbs / Fat", f"{st.session_state.carbs} g / {st.session_state.fats} g")

        st.markdown(
            """
            <div class="panel-card">
                <div class="section-title">Daily Nutrients To Take</div>
                <p class="soft-text">These are your full-day nutrition targets based on today's workout.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        nutrient_cols = st.columns(4)
        with nutrient_cols[0]:
            render_metric("Calories", f"{st.session_state.total_calories} kcal")
        with nutrient_cols[1]:
            render_metric("Protein", f"{st.session_state.protein} g")
        with nutrient_cols[2]:
            render_metric("Carbs", f"{st.session_state.carbs} g")
        with nutrient_cols[3]:
            render_metric("Fats", f"{st.session_state.fats} g")

        st.markdown(
            """
            <div class="panel-card">
                <div class="section-title">Divide These Nutrients Into 3 Meals</div>
                <p class="soft-text">Use these targets for breakfast, lunch, and dinner.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        split_cols = st.columns(3)
        for idx, meal_name in enumerate(["Breakfast", "Lunch", "Dinner"]):
            meal_values = st.session_state.meal_split[meal_name]
            with split_cols[idx]:
                st.markdown(
                    f"""
                    <div class="panel-card">
                        <div class="section-title">{meal_name}</div>
                        <p class="soft-text">
                            Calories: <strong>{meal_values["calories"]} kcal</strong><br>
                            Protein: <strong>{meal_values["protein"]} g</strong><br>
                            Carbs: <strong>{meal_values["carbs"]} g</strong><br>
                            Fats: <strong>{meal_values["fats"]} g</strong>
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    render_back_button(2)


def page_foods() -> None:
    if render_auth_required(3):
        return
    st.subheader("Suggested Food Names")

    if not st.session_state.suggested_meals:
        st.info("Please complete the exercise page first so the app can suggest foods.")
        render_back_button(3)
        return

    st.markdown(
        """
        <div class="panel-card">
            <div class="section-title">Suggested Foods For You</div>
            <p class="soft-text">Choose 1 food for breakfast, 1 for lunch, and 1 for dinner.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for meal_slot in ["Breakfast", "Lunch", "Dinner"]:
        options = st.session_state.suggested_meals.get(meal_slot, [])
        selected_index = st.session_state.selected_meals.get(meal_slot)

        st.markdown(
            f"""
            <div class="panel-card">
                <div class="section-title">{meal_slot}</div>
                <p class="soft-text">Pick one option for your {meal_slot.lower()}.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        for index, meal in enumerate(options):
            left, right = st.columns([5, 1])
            with left:
                selected_note = '<p class="soft-text"><strong>Selected</strong></p>' if selected_index == index else ""
                st.markdown(
                    f"""
                    <div class="food-card">
                        <div class="food-name">{meal["name"]}</div>
                        {selected_note}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with right:
                if st.button("Choose", key=f"{meal_slot}_{index}"):
                    st.session_state.selected_meals[meal_slot] = index
                    if len(st.session_state.selected_meals) == 3:
                        go_to_page(4)
                    st.rerun()

    if len(st.session_state.selected_meals) == 3:
        st.success("Breakfast, lunch, and dinner are selected. Open the recipe page to view all 3 recipes.")

    render_back_button(3)


def page_recipe() -> None:
    if render_auth_required(4):
        return
    st.subheader("Recipe Of Selected Food")

    if not st.session_state.suggested_meals:
        st.info("Please finish the exercise page first to generate food suggestions.")
        render_back_button(4)
        return

    if len(st.session_state.selected_meals) < 3:
        st.info("Please choose one food for breakfast, lunch, and dinner on the previous page first.")
        render_back_button(4)
        return

    for meal_slot in ["Breakfast", "Lunch", "Dinner"]:
        selected_index = st.session_state.selected_meals[meal_slot]
        meal = st.session_state.suggested_meals[meal_slot][selected_index]
        meal_target = st.session_state.meal_split.get(
            meal_slot,
            {"calories": 0, "protein": 0, "carbs": 0, "fats": 0},
        )
        st.markdown(
            f"""
            <div class="panel-card">
                <div class="section-title">{meal_slot}</div>
                <div class="food-name">{meal["name"]}</div>
                <div class="section-title">Meal Nutrient Target</div>
                <p class="soft-text">
                    Calories: <strong>{meal_target["calories"]} kcal</strong><br>
                    Protein: <strong>{meal_target["protein"]} g</strong><br>
                    Carbs: <strong>{meal_target["carbs"]} g</strong><br>
                    Fats: <strong>{meal_target["fats"]} g</strong>
                </p>
                <div class="section-title">Ingredients</div>
                <p class="soft-text">{meal["ingredients"]}</p>
                <div class="section-title">Recipe</div>
                <p class="soft-text">{meal["recipe"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_back_button(4)


apply_theme()
init_state()
try:
    init_database()
    st.session_state.db_ready = True
    st.session_state.db_error = ""
except Exception as exc:
    st.session_state.db_ready = False
    st.session_state.db_error = str(exc)
render_header()

page_labels = [
    "Login Page",
    "Body Details",
    "Exercise And Calories",
    "Suggested Food Name",
    "Recipe Page",
]

st.sidebar.title("Navigation")
st.sidebar.caption("Move between the app pages here.")
selected_page = st.sidebar.radio(
    "Go To",
    page_labels,
    index=int(st.session_state.current_page),
)
selected_index = page_labels.index(selected_page)
if selected_index != st.session_state.current_page:
    st.session_state.current_page = selected_index

if st.session_state.current_page == 0:
    page_profile()
elif st.session_state.current_page == 1:
    page_body_details()
elif st.session_state.current_page == 2:
    page_exercises()
elif st.session_state.current_page == 3:
    page_foods()
else:
    page_recipe()
