# Diabetes Nutrition and Glucose Coach

## Overview

This project is an interactive web application designed to support individuals in understanding how their dietary choices may impact blood glucose levels. The application allows users to input their meals and glucose readings, and in return provides structured, practical recommendations to support better day-to-day diabetes management.

The system is built using a rule-based decision framework grounded in commonly accepted glucose thresholds and nutritional patterns. The focus is on delivering simple, interpretable, and safety-aware guidance rather than predictive or diagnostic outputs.

---

## Features

* **Meal Analysis**
  Identifies key food components and classifies them into high-carbohydrate, moderate-carbohydrate, and supportive (protein and fiber-rich) categories.

* **Glucose Interpretation**
  Evaluates glucose readings across multiple ranges, including low, normal, elevated, high, and very high.

* **Context-Aware Recommendations**
  Provides actionable suggestions based on both meal composition and glucose level, including guidance on hydration, food choices, and activity.

* **Safety Considerations**
  Incorporates appropriate responses for low blood glucose, including immediate corrective steps and avoidance of unsafe actions such as exercise during hypoglycemia.

* **Interactive Interface**
  Built with Streamlit, enabling a simple and responsive user experience with real-time feedback.

---

## Technology Stack

* Python
* Streamlit
* Rule-based logic system for decision-making

---

## Project Structure

```
Diabetes-GenAI/
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## How to Run Locally

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the application:

```
streamlit run streamlit_app.py
```

---

## Live Application

https://diabetes-nutrition-glucose-coach-dy34fcbllgsxcjdhp3u9nk.streamlit.app/

---

## Design Approach

The application follows a rule-based approach to ensure consistent and interpretable outputs. Glucose thresholds are used to determine appropriate response categories, while food inputs are parsed and mapped to predefined nutritional groups.

The system is intentionally designed to avoid overgeneralization or medical claims. Instead, it focuses on providing structured guidance that can support informed decision-making in everyday scenarios.

---

## Limitations

* The system does not account for individual medical history, medication, or insulin use.
* Food analysis is based on keyword matching and may not capture all variations in diet.
* The recommendations are general in nature and not personalized to clinical standards.

---

## Disclaimer

This application is intended for educational and informational purposes only. It does not provide medical advice, diagnosis, or treatment. Users should consult a qualified healthcare professional for medical guidance.

---

## Author

Aarya Mirkale

