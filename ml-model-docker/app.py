import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

# Load Dataset
st.title("Mushroom Classification App 🍄")
st.write("This app predicts whether a mushroom is edible or poisonous.")

df = pd.read_csv("mushrooms.csv")

# Data preprocessing (example)
df = pd.get_dummies(df, drop_first=True)

# Train Model
X = df.drop("class_p", axis=1)
y = df["class_p"]

model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("mushroom_model.pkl", "wb") as file:
    pickle.dump(model, file)

# Load model for prediction
with open("mushroom_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

# User input form
st.sidebar.header("Mushroom Features")
user_input = {col: st.sidebar.selectbox(col, df[col].unique()) for col in X.columns}

# Convert input to DataFrame
user_df = pd.DataFrame([user_input])

# Make prediction
prediction = loaded_model.predict(user_df)
st.write(f"Prediction: {'Poisonous' if prediction[0] == 1 else 'Edible'} 🍄")
