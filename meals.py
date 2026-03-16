from __future__ import annotations


def suggest_meals(goal: str, workout_type: str) -> dict[str, list[dict[str, str]]]:
    weight_loss_breakfast = [
        {
            "name": "Moong Dal Chilla With Mint Curd",
            "ingredients": (
                "1/2 cup soaked moong dal, 1 green chili, 1 tbsp chopped onion, "
                "1 tbsp grated carrot, 1 tsp oil, 1/4 tsp cumin, 1/4 cup low-fat curd, "
                "1 tbsp mint chutney"
            ),
            "recipe": (
                "Blend soaked moong dal with chili and cumin. Mix in onion and carrot. "
                "Spread on a hot pan with a little oil and cook both sides. Serve with curd mixed with mint chutney."
            ),
        },
        {
            "name": "Paneer Bhurji With 2 Phulkas",
            "ingredients": (
                "100 g low-fat paneer, 1 small tomato, 1 small onion, 1/4 tsp turmeric, "
                "1/4 tsp garam masala, 1 tsp oil, 2 medium phulkas"
            ),
            "recipe": (
                "Saute onion and tomato in oil. Add spices and crumbled paneer, then cook for 3 to 4 minutes. "
                "Serve hot with 2 phulkas."
            ),
        },
        {
            "name": "Vegetable Dalia Bowl",
            "ingredients": (
                "1/2 cup broken wheat, 1 cup mixed vegetables, 1 tsp oil, 1/4 tsp mustard seeds, "
                "1/4 tsp turmeric, 1 1/2 cups water, salt to taste"
            ),
            "recipe": (
                "Roast dalia lightly. Temper mustard seeds in oil, add vegetables and turmeric, then add dalia and water. "
                "Cook until soft and serve warm."
            ),
        },
    ]

    weight_loss_lunch = [
        {
            "name": "Lauki Chana Dal With 2 Rotis",
            "ingredients": (
                "1 cup bottle gourd, 1/3 cup chana dal, 1 tsp oil, 1/4 tsp cumin, "
                "1 small tomato, 2 medium rotis"
            ),
            "recipe": (
                "Cook chana dal and lauki together until soft. Add a light tadka with cumin and tomato. "
                "Serve with 2 rotis."
            ),
        },
        {
            "name": "Grilled Paneer Salad Bowl",
            "ingredients": (
                "100 g paneer, 1 cup cucumber, 1 cup lettuce, 1/2 cup tomato, "
                "1 tsp olive oil, 1 tsp lemon juice, black pepper"
            ),
            "recipe": (
                "Grill paneer lightly. Toss vegetables with olive oil, lemon juice, and black pepper, "
                "then top with paneer."
            ),
        },
        {
            "name": "Mixed Veg Khichdi",
            "ingredients": (
                "1/4 cup rice, 1/4 cup moong dal, 1 cup mixed vegetables, 1 tsp ghee, "
                "1/4 tsp cumin, 2 cups water"
            ),
            "recipe": (
                "Cook rice, dal, and vegetables with cumin and ghee until soft. Serve warm as a light lunch."
            ),
        },
    ]

    weight_loss_dinner = [
        {
            "name": "Palak Paneer With 2 Phulkas",
            "ingredients": (
                "90 g paneer, 2 cups spinach, 1 tsp oil, 1 garlic clove, "
                "1/4 tsp cumin, 2 medium phulkas"
            ),
            "recipe": (
                "Cook spinach and blend lightly. Saute garlic and cumin, add paneer and spinach, "
                "then simmer and serve with 2 phulkas."
            ),
        },
        {
            "name": "Tofu Bhurji Bowl",
            "ingredients": (
                "120 g tofu, 1 small onion, 1 small tomato, 1/4 tsp turmeric, "
                "1 tsp oil, 1/2 cup sauteed vegetables"
            ),
            "recipe": (
                "Saute onion and tomato with spices, add crumbled tofu, and cook for 4 minutes. "
                "Serve with vegetables."
            ),
        },
        {
            "name": "Tomato Oats Soup With Sprouts",
            "ingredients": (
                "1/2 cup oats, 2 tomatoes, 1/4 cup boiled sprouts, 1 tsp oil, "
                "1 garlic clove, 2 cups water"
            ),
            "recipe": (
                "Cook tomatoes and garlic, blend into soup, then simmer with oats. "
                "Top with boiled sprouts before serving."
            ),
        },
    ]

    muscle_gain_breakfast = [
        {
            "name": "Chicken Rice Power Bowl",
            "ingredients": (
                "150 g chicken breast, 1 cup cooked rice, 1/2 cup curd, 1/2 cup cucumber, "
                "1 tsp ghee, 1/4 tsp chili powder, 1/4 tsp cumin powder"
            ),
            "recipe": (
                "Cook chicken with chili powder and cumin in ghee. Place over cooked rice and serve with curd "
                "and chopped cucumber on the side."
            ),
        },
        {
            "name": "Paneer Pulao With Boiled Eggs",
            "ingredients": (
                "120 g paneer, 1 cup cooked basmati rice, 1/4 cup peas, 1 tbsp chopped carrot, "
                "1 tsp oil, 2 boiled eggs, 1/4 tsp garam masala"
            ),
            "recipe": (
                "Saute vegetables and paneer in oil, add garam masala and cooked rice, and toss well. "
                "Serve with 2 boiled eggs for extra protein."
            ),
        },
        {
            "name": "Peanut Banana Oats Smoothie",
            "ingredients": (
                "1 banana, 40 g oats, 300 ml milk, 1 tbsp peanut butter, 4 almonds, 1 tsp honey"
            ),
            "recipe": (
                "Blend banana, oats, milk, peanut butter, almonds, and honey until smooth. "
                "Drink as a calorie-dense recovery meal."
            ),
        },
    ]

    muscle_gain_lunch = [
        {
            "name": "Chicken Dal Rice Plate",
            "ingredients": (
                "120 g chicken breast, 3/4 cup cooked rice, 1/2 cup dal, 1 tsp ghee, "
                "1/2 cup cucumber salad"
            ),
            "recipe": "Cook chicken with mild spices. Serve with warm dal, rice, and cucumber salad.",
        },
        {
            "name": "Paneer Paratha With Curd",
            "ingredients": (
                "2 stuffed paneer parathas, 1/2 cup curd, 1 tsp ghee, 1 tbsp chopped coriander"
            ),
            "recipe": (
                "Prepare paneer filling, stuff into dough, and cook parathas with a little ghee. "
                "Serve with curd."
            ),
        },
        {
            "name": "Rajma Rice With Egg Bhurji",
            "ingredients": (
                "3/4 cup rajma, 1 cup cooked rice, 2 eggs, 1 tsp oil, 1 small onion, 1 small tomato"
            ),
            "recipe": (
                "Serve rajma and rice together. Make quick egg bhurji with onion and tomato on the side."
            ),
        },
    ]

    muscle_gain_dinner = [
        {
            "name": "Soya Pulao Bowl",
            "ingredients": (
                "1 cup cooked rice, 1/2 cup soya chunks, 1/4 cup peas, 1 tsp oil, 1/4 tsp garam masala"
            ),
            "recipe": "Cook soya chunks and peas with spices, then toss with rice for a protein-rich dinner.",
        },
        {
            "name": "Egg Curry With 2 Rotis",
            "ingredients": (
                "3 boiled eggs, 1 small onion, 1 small tomato, 1 tsp oil, 1/4 tsp turmeric, 2 medium rotis"
            ),
            "recipe": (
                "Make a light onion-tomato curry, add boiled eggs, simmer briefly, and serve with 2 rotis."
            ),
        },
        {
            "name": "Paneer Millet Bowl",
            "ingredients": (
                "120 g paneer, 3/4 cup cooked millet, 1/2 cup vegetables, 1 tsp oil, 1/4 tsp black pepper"
            ),
            "recipe": "Saute paneer and vegetables with black pepper. Serve over cooked millet.",
        },
    ]

    maintain_breakfast = [
        {
            "name": "Rajma Rice Plate",
            "ingredients": (
                "3/4 cup cooked rajma, 3/4 cup cooked rice, 1 small onion, 1 small tomato, "
                "1 tsp oil, 1/4 tsp cumin, 1/4 tsp coriander powder"
            ),
            "recipe": (
                "Prepare a simple rajma masala with onion, tomato, cumin, and coriander powder. "
                "Serve with cooked rice for a balanced meal."
            ),
        },
        {
            "name": "Vegetable Upma With Curd",
            "ingredients": (
                "1/2 cup rava, 1 cup mixed vegetables, 1 tsp oil, 1/4 tsp mustard seeds, "
                "8 curry leaves, 1 1/4 cups water, 1/3 cup curd"
            ),
            "recipe": (
                "Roast rava. Temper mustard seeds and curry leaves in oil, cook vegetables, add water, "
                "then stir in rava until fluffy. Serve with curd."
            ),
        },
        {
            "name": "Tofu Stir-Fry Roti Roll",
            "ingredients": (
                "120 g tofu, 2 whole-wheat rotis, 1/2 cup capsicum, 1/4 cup onion, "
                "1 tsp oil, 1/4 tsp black pepper, 1 tbsp hung curd"
            ),
            "recipe": (
                "Stir-fry tofu, onion, and capsicum in oil with black pepper. Fill the rotis, "
                "top with hung curd, and roll before serving."
            ),
        },
    ]

    maintain_lunch = [
        {
            "name": "Dal Rice With Beetroot Salad",
            "ingredients": "1/2 cup dal, 3/4 cup cooked rice, 1/2 cup beetroot salad, 1 tsp ghee, cumin",
            "recipe": "Prepare simple dal tadka and serve with rice and fresh beetroot salad.",
        },
        {
            "name": "Curd Rice With Cucumber",
            "ingredients": (
                "1 cup cooked rice, 3/4 cup curd, 1/2 cup cucumber, 1 tsp oil, mustard seeds and curry leaves"
            ),
            "recipe": (
                "Mix rice with curd, then add a light mustard and curry leaf tempering. Serve chilled with cucumber."
            ),
        },
        {
            "name": "Vegetable Sambar With Idli",
            "ingredients": "2 idlis, 1 cup sambar, 1/2 cup mixed vegetables, 1 tsp oil",
            "recipe": "Prepare sambar with vegetables and serve hot with soft idlis.",
        },
    ]

    maintain_dinner = [
        {
            "name": "Chapati With Mixed Veg Curry",
            "ingredients": (
                "2 chapatis, 1 cup mixed vegetable curry, 1 tsp oil, 1/4 tsp cumin, 1/4 cup curd"
            ),
            "recipe": "Cook a simple mixed vegetable curry and serve with 2 chapatis and curd.",
        },
        {
            "name": "Paneer Soup And Toast",
            "ingredients": "80 g paneer, 2 tomatoes, 1 garlic clove, 1 tsp oil, 2 whole-grain toasts",
            "recipe": "Blend cooked tomatoes into soup, add paneer cubes, simmer briefly, and serve with toast.",
        },
        {
            "name": "Vegetable Oats Cheela",
            "ingredients": (
                "1/2 cup oats flour, 1/4 cup curd, 1/2 cup vegetables, 1 tsp oil, 1/4 tsp cumin"
            ),
            "recipe": "Mix oats flour, curd, and vegetables into a batter. Cook on a hot pan with a little oil.",
        },
    ]

    workout_boost = {
        "Strength": {
            "Breakfast": {
                "name": "Post-Workout Banana Milkshake",
                "ingredients": "1 banana, 250 ml milk, 1 tbsp peanut butter, 4 almonds",
                "recipe": "Blend all ingredients until smooth and serve chilled after training.",
            }
        },
        "Cardio": {
            "Breakfast": {
                "name": "Poha With Sprouts",
                "ingredients": "1 cup poha, 1/3 cup sprouts, 1 tbsp peanuts, 1 tsp oil, lemon juice",
                "recipe": "Cook poha with peanuts, fold in sprouts, and finish with lemon juice.",
            }
        },
        "HIIT": {
            "Dinner": {
                "name": "Banana Lassi Recovery Drink",
                "ingredients": "1 banana, 250 ml curd, 100 ml water, 1 tsp honey, 1 tsp chia seeds",
                "recipe": "Blend all ingredients and serve chilled as a recovery drink.",
            }
        },
        "Rest Day": {
            "Dinner": {
                "name": "Palak Dal With 2 Rotis",
                "ingredients": "1/2 cup toor dal, 1 cup spinach, 1 tsp oil, cumin, garlic, 2 rotis",
                "recipe": "Cook dal, add spinach tadka, and serve with 2 rotis.",
            }
        },
    }

    if goal == "Weight Loss":
        meal_plan = {
            "Breakfast": weight_loss_breakfast,
            "Lunch": weight_loss_lunch,
            "Dinner": weight_loss_dinner,
        }
    elif goal == "Muscle Gain":
        meal_plan = {
            "Breakfast": muscle_gain_breakfast,
            "Lunch": muscle_gain_lunch,
            "Dinner": muscle_gain_dinner,
        }
    else:
        meal_plan = {
            "Breakfast": maintain_breakfast,
            "Lunch": maintain_lunch,
            "Dinner": maintain_dinner,
        }

    boost = workout_boost.get(workout_type, {})
    for slot, boosted_meal in boost.items():
        meal_plan[slot] = [boosted_meal] + meal_plan[slot][:2]

    return meal_plan
