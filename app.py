import streamlit as st
import pickle
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Disease Prediction App", page_icon="🩺")

# Hiding Streamlit extras
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Background Images for Different Diseases
background_images = {
    'Malaria Prediction': "https://i.postimg.cc/DwYqmDXN/medical-photo.jpg",
    'Aortic Disease Prediction': "https://i.postimg.cc/j5LZvvzX/maleria.webp",
}

# Sidebar Selection
selected = st.sidebar.selectbox("Select Disease to Predict", [
    'Malaria Prediction',
    "Aortic Disease Prediction"
])

# Apply Background Image Based on Selection
background_image_url = background_images.get(selected, background_images['Malaria Prediction'])

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url({background_image_url});
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(255, 255, 255, 0.6);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load Models
models = {
    'malaria': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'Aortic Disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
}

st.title("🩺 Disease Prediction System")
st.write("Predict common diseases using machine learning models.")

def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)

# Malaria Prediction Page

if selected == 'Malaria Prediction':
    st.title('Malaria')
    st.write("Enter the following details to predict diabetes:")

    Fever = display_input('Fever', 'Enter number of times pregnant', 'Pregnancies', 'number')
    Glucose = display_input('Glucose Level', 'Enter glucose level', 'Glucose', 'number')
    BloodPressure = display_input('Blood Pressure value', 'Enter blood pressure value', 'BloodPressure', 'number')
    Headache = display_input('Headache', 'Enter skin thickness value', 'SkinThickness', 'number')
    Diarrhea = display_input('Diarrhea', 'Enter insulin level', 'Insulin', 'number')
    BodyTemperature  = display_input('Body Temperature ', 'Enter Body Mass Index value', 'BMI', 'number')
    Headache = display_input('Fever Pedigree Function value', 'Enter malaria pedigree function value', 'malariaPedigreeFunction', 'number')
    Age = display_input('Age of the Person', 'Enter age of the person', 'Age', 'number')

    diab_diagnosis = ''
    if st.button('malaria Test Result'):
        diab_prediction = models['malaria'].predict([[Fever , Glucose, BloodPressure, Headache , Diarrhea , BodyTemperature, Headache , Age]])
        diab_diagnosis = 'The person is malaria' if diab_prediction[0] == 1 else 'The person is not malaria'
        st.success(diab_diagnosis)

# Aortic Disease Prediction Page
if selected == 'Aortic Disease Prediction':
    st.title('Aortic Disease')
    st.write("Enter the following details to predict aortic disease:")

    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex (1 = male; 0 = female)', 'Enter sex of the person', 'sex', 'number')
    cp = display_input('Chest Pain types (0, 1, 2, 3)', 'Enter chest pain type', 'cp', 'number')
    trestbps = display_input('Resting Blood Pressure', 'Enter resting blood pressure', 'trestbps', 'number')
    chol = display_input('Serum Cholesterol in mg/dl', 'Enter serum cholesterol', 'chol', 'number')
    fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', 'Enter fasting blood sugar', 'fbs', 'number')
    restecg = display_input('Resting Electrocardiographic results (0, 1, 2)', 'Enter resting ECG results', 'restecg', 'number')
    thalach = display_input('Maximum Heart Rate achieved', 'Enter maximum heart rate', 'thalach', 'number')
    exang = display_input('Exercise Induced Angina (1 = yes; 0 = no)', 'Enter exercise induced angina', 'exang', 'number')
    oldpeak = display_input('ST depression induced by exercise', 'Enter ST depression value', 'oldpeak', 'number')
    slope = display_input('Slope of the peak exercise ST segment (0, 1, 2)', 'Enter slope value', 'slope', 'number')
    ca = display_input('Major vessels colored by fluoroscopy (0-3)', 'Enter number of major vessels', 'ca', 'number')
    thal = display_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', 'Enter thal value', 'thal', 'number')

    heart_diagnosis = ''
    if st.button('Aortic Disease Test Result'):
        heart_prediction = models['Aortic Disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        heart_diagnosis= 'The person has Aortic Disease' if heart_prediction[0] == 1 else 'The person does not have Aortic Disease'
        st.success(heart_diagnosis)                      