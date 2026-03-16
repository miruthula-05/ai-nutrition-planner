# AI Nutrition Planner 🥗💪

AI Nutrition Planner is a Streamlit-based web application that generates personalized nutrition recommendations based on user body details, workout activity, and training goals.

The application guides users through multiple pages and calculates daily calorie needs, macronutrient distribution, and meal suggestions.

## Live Demo 🚀

Try the deployed application here:

🔗 **AI Nutrition Planner:**
https://ai-nutrition-planner-1.onrender.com

---

## Tech Stack

* Python
* Streamlit
* MySQL
* SQL
* Rule-based nutrition calculation

---

## Features

* Multi-user sign up and login with MySQL
* 5-page guided workflow
* Exercise-based calorie estimation
* Daily calorie requirement calculation
* Macronutrient recommendation (Protein, Carbs, Fat)
* Meal nutrient split for breakfast, lunch, and dinner
* Indian meal suggestions with recipe steps
* Clean and beginner-friendly project structure

---

## Project Structure

```
ai-nutrition-planner/
|-- app.py
|-- logic.py
|-- db.py
|-- auth.py
|-- meals.py
|-- state.py
|-- theme.py
|-- requirements.txt
|-- README.md
`-- images/
```

---

## App Pages

1. Login page
2. Body details page
3. Exercise and calories page
4. Suggested food names page
5. Recipe page

---

## Inputs

The user provides:

* Name
* Email
* Phone number
* Password
* Gender
* Height
* Weight
* Training goal
* Exercises performed
* Sets and repetitions

---

## How the Logic Works

1. Estimate daily calorie requirement from body weight
2. Adjust calories using height and training goal
3. Calculate calories burned from exercises
4. Combine total energy expenditure
5. Split calories into macronutrients
6. Generate breakfast, lunch, and dinner suggestions
7. Provide Indian recipe steps for selected meals

---

## MySQL Setup

Set these environment variables:

```
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=ai_nutrition_planner
```

The application automatically creates the database and `users` table if they do not exist.

---

## Installation

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows:

```
venv\Scripts\activate
```

macOS / Linux:

```
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
streamlit run app.py
```

---

## Example Use Cases

* Weight loss planning
* Muscle gain nutrition estimation
* Tracking exercise-based calorie expenditure
* Quick maintenance calorie estimation

---

## Disclaimer

This project is intended for educational purposes only and does not replace professional medical or dietary advice.

---

## Author

**Miruthula Sri A**

B.E Artificial Intelligence and Machine Learning

