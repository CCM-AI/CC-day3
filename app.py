import streamlit as st
from datetime import datetime

# Placeholder functions for risk algorithms
def calculate_cardio_risk(age, systolic_bp, smoker, cholesterol):
    risk_score = (age * 0.1) + (systolic_bp * 0.05) + (10 if smoker else 0) + (cholesterol * 0.02)
    if risk_score > 15:
        return "High"
    elif risk_score > 10:
        return "Moderate"
    else:
        return "Low"

def calculate_diabetes_risk(bmi, age, family_history, fasting_glucose):
    risk_score = (bmi * 0.3) + (age * 0.1) + (10 if family_history else 0) + (fasting_glucose * 0.02)
    if risk_score > 20:
        return "High"
    elif risk_score > 15:
        return "Moderate"
    else:
        return "Low"

def calculate_copd_risk(smoking_years, age, fev1):
    risk_score = (smoking_years * 0.5) + (age * 0.2) - (fev1 * 0.1)
    if risk_score > 25:
        return "High"
    elif risk_score > 15:
        return "Moderate"
    else:
        return "Low"

def calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1):
    risk_score = (frequency_of_symptoms * 2) + (nighttime_symptoms * 3) + (inhaler_use * 1.5) - (fev1 * 0.1)
    if risk_score > 20:
        return "High"
    elif risk_score > 10:
        return "Moderate"
    else:
        return "Low"

# Streamlit App Layout
st.title("Chronic Condition Risk Stratification and Personalized Care Plan")
st.write("This application stratifies risk for chronic conditions and provides a personalized care plan with detailed monitoring, follow-up, and outcome evaluation according to evidence-based guidelines.")

# Define tabs for each condition
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Cardiovascular Risk", "Diabetes Risk", "COPD Risk", "Asthma Risk", "Personalized Care Plan"])

# Results dictionary to store risk levels for each condition
results = {}

# Cardiovascular Risk Tab
with tab1:
    st.header("Cardiovascular Risk Assessment")
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    systolic_bp = st.slider("Systolic Blood Pressure (mmHg)", 90, 200, 120)
    cholesterol = st.slider("Total Cholesterol (mg/dL)", 100, 300, 180)
    smoker = st.radio("Smoking Status", options=["Non-smoker", "Current smoker"])

    if st.button("Calculate Cardiovascular Risk"):
        cardio_risk = calculate_cardio_risk(age, systolic_bp, smoker == "Current smoker", cholesterol)
        st.write(f"**Cardiovascular Risk Level**: {cardio_risk}")
        results["Cardiovascular"] = cardio_risk

# Diabetes Risk Tab
with tab2:
    st.header("Diabetes Risk Assessment")
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
    family_history = st.radio("Family History of Diabetes", options=["Yes", "No"])
    fasting_glucose = st.number_input("Fasting Glucose (mg/dL)", min_value=50, max_value=300, value=90)

    if st.button("Calculate Diabetes Risk"):
        diabetes_risk = calculate_diabetes_risk(bmi, age, family_history == "Yes", fasting_glucose)
        st.write(f"**Diabetes Risk Level**: {diabetes_risk}")
        results["Diabetes"] = diabetes_risk

# COPD Risk Tab
with tab3:
    st.header("COPD Risk Assessment")
    smoking_years = st.number_input("Years of Smoking (if applicable)", min_value=0, max_value=60, value=0)
    fev1_copd = st.number_input("FEV1 (%) - COPD", min_value=20, max_value=100, value=80)

    if st.button("Calculate COPD Risk"):
        copd_risk = calculate_copd_risk(smoking_years, age, fev1_copd)
        st.write(f"**COPD Risk Level**: {copd_risk}")
        results["COPD"] = copd_risk

# Asthma Risk Tab
with tab4:
    st.header("Asthma Risk Assessment")
    frequency_of_symptoms = st.slider("Frequency of Asthma Symptoms (days per week)", 0, 7, 3)
    nighttime_symptoms = st.slider("Nighttime Symptoms (days per week)", 0, 7, 1)
    inhaler_use = st.slider("Inhaler Use (days per week)", 0, 7, 2)
    fev1_asthma = st.number_input("FEV1 (%) - Asthma", min_value=20, max_value=100, value=80)

    if st.button("Calculate Asthma Risk"):
        asthma_risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1_asthma)
        st.write(f"**Asthma Risk Level**: {asthma_risk}")
        results["Asthma"] = asthma_risk

# Personalized Care Plan Tab
with tab5:
    st.header("Personalized Care Plan")
    for condition, risk in results.items():
        st.subheader(f"{condition} Risk: {risk}")

        # Define the care plan based on the risk level
        if risk == "High":
            st.error(f"{condition} Risk is High.")
            st.write("### Recommended Care Plan:")
            st.write("- **Self-management support**: Comprehensive lifestyle modifications, including diet, physical activity, and medication adherence with regular education sessions.")
            
            # Monitoring Plan
            st.write("### Monitoring Plan:")
            st.write("- **Frequency**: Monthly clinic visits.")
            st.write("- **Tests**: Regular blood work (e.g., lipid profile, HbA1c for diabetes, pulmonary function for COPD, peak flow for asthma).")
            st.write("- **Technology Use**: Remote health monitoring tools such as wearable devices for blood pressure, glucose, or peak flow tracking for asthma.")
            
            # Follow-Up Plan
            st.write("### Follow-Up Plan:")
            st.write("- **Frequency**: Every 1-3 months depending on condition and symptom progression.")
            st.write("- **Content**: Adjust treatment plans as needed and review adherence to medication and lifestyle changes.")
            
            # Outcome Evaluation Plan
            st.write("### Outcome Evaluation Plan:")
            st.write("- **Timeframe**: Quarterly evaluations for risk factors like blood pressure, glucose levels, lung function, or asthma control.")
            st.write("- **Adjustments**: Intensify interventions if risk factors are not improving.")

        elif risk == "Moderate":
            st.warning(f"{condition} Risk is Moderate.")
            st.write("### Recommended Care Plan:")
            st.write("- **Self-management support**: Lifestyle counseling with moderate modifications such as balanced diet, reduced smoking exposure, and physical activity.")
            
            # Monitoring Plan
            st.write("### Monitoring Plan:")
            st.write("- **Frequency**: Every 3-6 months.")
            st.write("- **Tests**: Basic blood work and relevant condition-specific tests (e.g., HbA1c for diabetes, spirometry for COPD, peak flow for asthma).")
            st.write("- **Home Tracking**: Encourage at-home monitoring for blood pressure, weight, or peak flow as appropriate.")
            
            # Follow-Up Plan
            st.write("### Follow-Up Plan:")
            st.write("- **Frequency**: Every 3-6 months with healthcare provider.")
            st.write("- **Content**: Review progress on lifestyle changes and risk factors, adjust care plan if needed.")
            
            # Outcome Evaluation Plan
            st.write("### Outcome Evaluation Plan:")
            st.write("- **Timeframe**: Semi-annual assessment of progress in risk factors.")
            st.write("- **Adjustments**: Moderate intensification of lifestyle or medication therapy if no improvement is observed.")

        else:  # Low Risk
            st.success(f"{condition} Risk is Low.")
            st.write("### Recommended Care Plan:")
            st.write("- **Self-management support**: Encourage a healthy lifestyle, regular physical activity, and preventive practices.")
            
            # Monitoring Plan
            st.write("### Monitoring Plan:")
            st.write("- **Frequency**: Annual check-ups.")
            st.write("- **Tests**: Basic blood work and periodic check-ups depending on age and risk factors.")
            
            # Follow-Up Plan
            st.write("### Follow-Up Plan:")
            st.write("- **Frequency**: Yearly follow-up with healthcare provider.")
            st.write("- **Content**: Assess maintenance of healthy habits and address any emerging concerns.")
            
            # Outcome Evaluation Plan
            st.write("### Outcome Evaluation Plan:")
            st.write("- **Timeframe**: Annual evaluation for emerging risk factors.")
            st.write("- **Adjustments**: Increase monitoring frequency if any new risk factors are identified.")

    st.write("### Date and Time of Assessment")
    st.write("Assessment Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
