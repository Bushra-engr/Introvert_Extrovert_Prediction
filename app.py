import streamlit as st
import numpy as np
import joblib
import pandas as pd

# 1. Model Load karo
model = joblib.load('personality_model.pkl')

# 2. App ka Title aur Design
st.set_page_config(page_title="Personality Predictor", page_icon="🧠")
st.title("🧠 Introvert vs Extrovert Predictor")
st.write("Answer a few questions to know your personality type!")

# 3. User Inputs (Form banate hain)
with st.form("my_form"):
    # Numeric Inputs
    age = st.number_input("Age", min_value=10, max_value=100, value=25)
    
    # Sliders for Scores (Assuming 1-10 scale based on your data)
    time_alone = st.slider("Time Spent Alone (Hours/Day)", 0, 11,2)
    social_events = st.slider("Social Events Attended (Per Week)", 0, 10, 2)
    going_out = st.slider("Going Out Frequency (Scale 1-10)", 1, 10, 5)
    friends = st.number_input("Friends Circle Size", min_value=0, max_value=20, value=10)
    post_freq = st.slider("Social Media Post Frequency (Scale 0-10)", 0, 10, 5)
    # Categorical Inputs (Yes/No)
    # Humein inhe 1/0 mein badalna padega kyunki model numbers samajhta hai
    stage_fear = st.selectbox("Do you have Stage Fear?", ["No", "Yes"])
    drained = st.selectbox("Do you feel drained after socializing?", ["No", "Yes"])
    
    # Submit Button
    submitted = st.form_submit_button("Predict Personality")

# 4. Logic jab button dabega
if submitted:
    # Yes/No ko 1/0 mein convert karo
    stage_fear_val = 1 if stage_fear == "Yes" else 0
    drained_val = 1 if drained == "Yes" else 0
    
    # Dataframe banao (Model ko yahi format chahiye)
    # IMPORTANT: Columns ka order wahi hona chahiye jo training ke time tha!
    input_data = pd.DataFrame({
        'Time_spent_Alone': [time_alone],
        'Social_event_attendance': [social_events],
        'Going_outside': [going_out],
        'Friends_circle_size': [friends],
        'Post_frequency': [post_freq],
        'Stage_fear_Yes': [stage_fear_val], # Check kar lena tumhare column ka naam yahi hai na?
        'Drained_after_socializing_Yes': [drained_val]
        # Agar aur columns the training mein, toh unhe bhi yahan add karo 0 value ke saath
    })

    # Prediction
    prediction = model.predict(input_data)
    
    # Result Dikhana
    st.markdown("---")
    if prediction[0] == 1: # Assuming 1 = Extrovert
        st.success("🎉 You are an **Extrovert**!")
        st.balloons()
    else:
        st.info("🧘 You are an **Introvert**!")