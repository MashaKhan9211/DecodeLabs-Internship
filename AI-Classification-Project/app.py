import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="AI Flower Classifier",
    page_icon="🌸",
    layout="wide"
)

# ---------------------------
# Title
# ---------------------------
st.title("🌸 AI Flower Classification")

st.write("Welcome to Project 2 of DecodeLabs AI Internship.")

# ---------------------------
# Load Dataset
# ---------------------------
iris = load_iris()

# Convert Dataset to DataFrame
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

# Add Flower Name Column
df["Flower"] = [
    iris.target_names[i]
    for i in iris.target
]

# Features (Inputs)
X = iris.data

# Target (Outputs)
y = iris.target

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create KNN Model
model = KNeighborsClassifier(n_neighbors=3)

# Train Model
model.fit(X_train, y_train)

# Test Model
y_pred = model.predict(X_test)

# Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)
# ---------------------------
# Dataset Information
# ---------------------------
st.header("📊 Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Samples", len(df))

with col2:
    st.metric("Features", len(iris.feature_names))

with col3:
    st.metric("Classes", len(iris.target_names))

# ---------------------------
# Preview Dataset
# ---------------------------
st.header("📄 Dataset Preview")

st.dataframe(df)
st.header("🤖 Model Performance")

st.success("Model Trained Successfully!")

st.metric(
    label="Accuracy",
    value=f"{accuracy*100:.2f}%"
)

# ---------------------------
# Prediction Section
# ---------------------------

st.header("🔍 Predict Flower")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input(
        "Sepal Length (cm)",
        value=5.1
    )

    sepal_width = st.number_input(
        "Sepal Width (cm)",
        value=3.5
    )

with col2:
    petal_length = st.number_input(
        "Petal Length (cm)",
        value=1.4
    )

    petal_width = st.number_input(
        "Petal Width (cm)",
        value=0.2
    )

# Predict Button
if st.button("🔍 Predict Flower"):

    prediction = model.predict([[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]])

    flower = iris.target_names[prediction[0]]

    st.success(f"🌸 Predicted Flower: {flower.title()}")

# ---------------------------
# Feature Names
# ---------------------------
st.header("🌼 Feature Description")


st.write("""
- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)
""")

# ---------------------------
# Flower Classes
# ---------------------------
st.header("🌸 Flower Classes")

for flower in iris.target_names:
    st.success(flower.title())