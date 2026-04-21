import streamlit as st

st.set_page_config(page_title="AI Diabetes Nutrition & Glucose Coach", layout="centered")

FOOD_CATEGORIES = {
    "high_carb_high_sugar": {
        "score": 2,
        "label": "high-carb/high-sugar",
        "items": [
            "white rice", "fried rice", "biryani", "pulao",
            "pasta", "noodles", "ramen", "mac and cheese",
            "white bread", "bun", "burger bun", "bagel",
            "fries", "chips", "nachos", "crackers",
            "pizza", "burger", "sandwich",
            "soda", "coke", "pepsi", "sprite",
            "juice", "sweet tea", "milkshake", "smoothie",
            "cake", "ice cream", "brownie", "cookie", "dessert",
            "donut", "pastry", "gulab jamun", "halwa", "kheer",
            "chocolate", "candy", "jam", "honey", "syrup"
        ]
    },
    "moderate_carb": {
        "score": 1,
        "label": "moderate-carb",
        "items": [
            "rice", "brown rice", "quinoa", "oats", "oatmeal",
            "granola", "muesli", "corn", "sweet corn",
            "potato", "sweet potato",
            "roti", "chapati", "paratha", "naan",
            "idli", "dosa", "upma", "poha",
            "beans", "rajma", "chole", "lentils", "dal",
            "banana", "mango", "grapes", "pineapple",
            "wrap", "tortilla", "whole wheat bread", "cereal"
        ]
    },
    "lean_protein_low_carb": {
        "score": -1,
        "label": "lean-protein/low-carb",
        "items": [
            "egg", "eggs", "egg whites",
            "chicken", "grilled chicken", "chicken breast", "tandoori chicken",
            "fish", "salmon", "tuna", "shrimp",
            "turkey", "tofu", "paneer", "greek yogurt",
            "curd", "cottage cheese", "cheese",
            "omelette", "boiled egg"
        ]
    },
    "vegetables_fiber": {
        "score": -1,
        "label": "vegetables/fiber-rich",
        "items": [
            "salad", "vegetables", "veggies",
            "broccoli", "spinach", "lettuce", "cucumber",
            "tomato", "onion", "bell pepper", "capsicum",
            "cauliflower", "cabbage", "zucchini", "okra",
            "beans", "green beans", "mushroom", "carrot"
        ]
    },
    "healthy_fats": {
        "score": -1,
        "label": "healthy-fat/supportive",
        "items": [
            "avocado", "nuts", "almonds", "walnuts",
            "peanut butter", "seeds", "chia", "flax",
            "olive oil", "hummus"
        ]
    }
}


def analyze_food_rules(food_text: str) -> dict:
    lower = f" {food_text.lower()} "
    found = []
    score = 0

    for category in FOOD_CATEGORIES.values():
        for item in category["items"]:
            if f" {item.lower()} " in lower or item.lower() in lower:
                found.append({
                    "item": item,
                    "label": category["label"],
                    "score": category["score"]
                })
                score += category["score"]

    seen = set()
    deduped = []
    for match in found:
        if match["item"] not in seen:
            seen.add(match["item"])
            deduped.append(match)

    high_items = [x["item"] for x in deduped if x["score"] == 2]
    moderate_items = [x["item"] for x in deduped if x["score"] == 1]
    supportive_items = [x["item"] for x in deduped if x["score"] == -1]

    if score >= 4:
        impact = "high"
    elif score >= 1:
        impact = "moderate"
    else:
        impact = "balanced"

    return {
        "score": score,
        "impact": impact,
        "high_items": high_items,
        "moderate_items": moderate_items,
        "supportive_items": supportive_items,
    }


def fallback_result(rule_analysis: dict, glucose_value: float, time_of_day: str) -> dict:
    impact = rule_analysis["impact"]

    if glucose_value < 70:
        glucose_msg = f"{glucose_value} mg/dL is low blood sugar. This needs prompt treatment."
        actions = [
            "Take 15 grams of fast-acting carbohydrate such as juice, glucose tablets, or regular soda",
            "Wait 15 minutes and recheck your glucose",
            "If still below 70 mg/dL, repeat the 15-15 rule",
            "Do not walk or exercise until your glucose is back in a safer range"
        ]
        next_meal = "After recovery, have a balanced meal or snack with carbohydrates and protein."
        exercise = "Do not exercise right now. Treat the low first."

        if glucose_value < 54:
            glucose_msg = f"{glucose_value} mg/dL is very low and may be dangerous."
            actions.append("Seek urgent medical help if symptoms are severe or you cannot safely manage the low")

    elif glucose_value <= 140:
        glucose_msg = f"{glucose_value} mg/dL is in a reasonable range for many situations, though personal targets can vary."

        if impact == "high":
            actions = [
                "Drink water",
                "Take a short 10–15 minute walk after the meal",
                "Try a lighter-carb next meal"
            ]
        elif impact == "moderate":
            actions = [
                "Stay hydrated",
                "Light movement after the meal may help",
                "Keep monitoring patterns over time"
            ]
        else:
            actions = [
                "Maintain your current balanced habits",
                "Keep portions steady",
                "Monitor your response to similar meals"
            ]

        next_meal = "Balanced meal with protein, fiber, and controlled carbs."
        exercise = "A 10–15 minute walk after meals can be helpful."

    elif glucose_value <= 180:
        glucose_msg = f"{glucose_value} mg/dL is somewhat elevated and worth monitoring, especially after meals."
        actions = [
            "Drink water",
            "Take a short walk after your meal if appropriate",
            "Avoid sugary foods or extra carbs in your next meal"
        ]
        next_meal = "Choose a lower-carb next meal with protein and vegetables."
        exercise = "Light walking may help support glucose control."

    elif glucose_value <= 250:
        glucose_msg = f"{glucose_value} mg/dL is high and deserves closer attention, especially if this is not typical for you."
        actions = [
            "Drink water unless a clinician has told you otherwise",
            "Avoid more sugary or high-carb foods right now",
            "Recheck your glucose later if that matches your routine"
        ]
        next_meal = "Your next meal should be lighter and more balanced, with protein, vegetables, and minimal refined carbs."
        exercise = "Light movement only if you feel okay and know it is safe for you."

    else:
        glucose_msg = f"{glucose_value} mg/dL is very high and may need prompt medical attention depending on your symptoms and care plan."
        actions = [
            "Do not eat more sugary foods",
            "Hydrate if appropriate",
            "Follow your doctor’s guidance for high glucose readings",
            "Seek urgent medical advice if you feel unwell or this is unusually high for you"
        ]
        next_meal = "Wait and follow your care plan; when eating next, choose a very light, balanced meal."
        exercise = "Avoid exercise until you know it is safe, especially if you feel unwell."

    if impact == "high":
        meal_msg = f"This {time_of_day.lower()} appears higher impact because it includes foods that may raise glucose more quickly."
    elif impact == "moderate":
        meal_msg = f"This {time_of_day.lower()} appears moderate impact, with some carbohydrate-containing foods that may affect glucose."
    else:
        meal_msg = f"This {time_of_day.lower()} appears relatively balanced based on the foods detected."

    return {
        "meal_assessment": meal_msg,
        "glucose_status": glucose_msg,
        "recommended_action": actions,
        "next_meal_suggestion": next_meal,
        "light_exercise": exercise,
        "disclaimer": "This is not medical advice. Please consult a healthcare professional for personal guidance."
    }


st.title("Diabetes Nutrition & Glucose Coach")
st.write("Enter what you ate and your glucose reading to get simple, supportive guidance.")

food = st.text_area("What did you eat?", placeholder="Example: chicken tandoori, 2 roti")
glucose = st.number_input("Enter glucose level (mg/dL)", min_value=1.0, step=1.0)

time_of_day = st.selectbox(
    "When was this meal?",
    ["Breakfast", "Lunch", "Dinner", "Snack"]
)

if st.button("Analyze"):
    if not food.strip():
        st.error("Please enter what you ate.")
    else:
        rule_analysis = analyze_food_rules(food)
        result = fallback_result(rule_analysis, glucose, time_of_day)

        st.subheader("Meal Context")
        st.write(f"Time of day: {time_of_day}")

        st.subheader("Meal Impact Category")
        st.write(rule_analysis["impact"].title())

        st.subheader("Detected Food Pattern")
        st.write(f"**High-impact items:** {', '.join(rule_analysis['high_items']) if rule_analysis['high_items'] else 'None'}")
        st.write(f"**Moderate items:** {', '.join(rule_analysis['moderate_items']) if rule_analysis['moderate_items'] else 'None'}")
        st.write(f"**Supportive items:** {', '.join(rule_analysis['supportive_items']) if rule_analysis['supportive_items'] else 'None'}")

        st.subheader("Meal Analysis")
        st.write(result["meal_assessment"])

        st.subheader("Glucose Insight")
        st.write(result["glucose_status"])

        st.subheader("Recommended Actions")
        for action in result["recommended_action"]:
            st.write(f"- {action}")

        st.subheader("Next Meal Suggestion")
        st.write(result["next_meal_suggestion"])

        st.subheader("Light Exercise")
        st.write(result["light_exercise"])

        st.warning(result["disclaimer"])