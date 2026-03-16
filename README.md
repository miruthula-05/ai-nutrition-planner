# AI Nutrition Planner

AI Nutrition Planner is a beginner-friendly Streamlit web application that guides the user through separate pages and then gives personalized nutrition recommendations.

The app uses rule-based logic to estimate:

- Daily calorie needs
- Calories burned from exercise
- Protein intake
- Carbohydrate intake
- Fat intake
- 3-meal nutrient split
- 3 food choices for each meal with recipe steps

## Features

- Easy-to-use web interface
- Minimal custom UI theme
- 5-page guided workflow
- Personal profile saved once
- Multi-user sign up and login with MySQL
- Automatic next-page flow after save
- Back button at the bottom of each page
- Exercise, sets, and reps based calorie estimation
- Simple nutrition calculations
- Daily nutrients divided into breakfast, lunch, and dinner targets
- 3 suggested food choices for breakfast, lunch, and dinner
- Indian recipe suggestions with quantitative ingredients
- Beginner-friendly Python project structure
- Clean and well-commented code

## Project Structure

```text
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

## App Pages

The app is divided into 5 pages:

1. Login page
2. Body details page
3. Exercise and calories page
4. Suggested food names page
5. Recipe page

## Inputs

The user enters:

- Name
- Email
- Phone number
- Password
- Gender
- Height
- Weight
- Purpose of training
- Number of exercises done
- Each exercise type
- Each exercise name
- Reps per set for each exercise
- Number of sets for each exercise

## How the Logic Works

The app follows a simple rule-based approach:

1. Estimate daily calorie requirement from weight
2. Add a small adjustment for height
3. Log multiple exercises for the day
4. Estimate calories burned for each exercise from its type, sets, reps, and body weight
5. Add total calories burned into the nutrition plan
6. Adjust calories for the selected goal
7. Split calories into protein, carbs, and fats
8. Suggest 3 Indian food choices for breakfast, lunch, and dinner
9. Show the recipes for the selected breakfast, lunch, and dinner foods

## MySQL Setup

Set these environment variables before running the app:

```bash
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=ai_nutrition_planner
```

The app will automatically create the database and `users` table if they do not exist.

## Installation

1. Create and activate a virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run app.py
```

## Example Use Cases

- Someone trying to lose weight and stay in a calorie deficit
- Someone training for muscle gain and needing more protein
- Someone who wants to log multiple exercises and see calories burned for each one
- Someone who wants a quick estimate for maintenance calories

## Important Note

This project is designed for learning and demonstration purposes. It does not replace advice from a doctor or registered dietitian.
