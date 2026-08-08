🩺 Medical Diagnosis Using AI – Disease Prediction

An AI-powered medical disease prediction application that uses Machine Learning and Streamlit to analyze patient health parameters and provide disease prediction results through an interactive web interface.

📌 Project Overview

Medical Diagnosis Using AI – Disease Prediction is a machine learning-based healthcare application developed to demonstrate how predictive models can be integrated into a user-friendly web application.

The system allows users to enter medical and health-related parameters and obtain predictions using pre-trained machine learning models. The application is developed using Python, Scikit-learn, Pandas, NumPy, and Streamlit.

The project currently provides prediction interfaces for:

🦠 Malaria Prediction
❤️ Aortic Disease Prediction

The trained models are loaded into the Streamlit application and used to generate predictions based on the input provided by the user.

Note: This project is developed for educational and research purposes. Predictions should not be considered a substitute for professional medical diagnosis or clinical advice.

🎯 Objectives
Develop a machine learning-based disease prediction system.
Process and analyze medical datasets.
Train and save machine learning models for prediction.
Integrate trained models into a web application.
Provide an interactive interface for entering patient information.
Demonstrate the practical application of AI and Machine Learning in healthcare.
🚀 Key Features
🦠 Malaria Prediction

The application provides a dedicated interface where users can enter health-related parameters such as:

Fever
Glucose Level
Blood Pressure
Headache
Diarrhea
Body Temperature
Age

The trained machine learning model processes the input and displays the prediction result.

❤️ Aortic Disease Prediction

The application provides another prediction interface using medical parameters including:

Age
Sex
Chest Pain Type
Resting Blood Pressure
Serum Cholesterol
Fasting Blood Sugar
Resting ECG Results
Maximum Heart Rate
Exercise-Induced Angina
ST Depression
Exercise ST Segment Slope
Major Vessels
Thalassemia-related value

The trained model analyzes these parameters and returns the prediction result.

🖥️ Interactive Web Interface

The application is built using Streamlit, providing:

Simple user interface
Sidebar disease selection
Input fields for medical parameters
Interactive prediction buttons
Real-time prediction results
Disease-specific page content
🧠 Machine Learning Workflow

The project follows a standard machine learning workflow:

Medical Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Selection
      │
      ▼
Train/Test Split
      │
      ▼
Machine Learning Model
      │
      ▼
Model Evaluation
      │
      ▼
Save Trained Model
      │
      ▼
Streamlit Application
      │
      ▼
User Input
      │
      ▼
Disease Prediction
🛠️ Technologies Used
Programming Language
Python
Machine Learning & Data Processing
Scikit-learn
Pandas
NumPy
Web Application
Streamlit
Streamlit Option Menu
Development Tools
Google Colab
Visual Studio Code
Git
GitHub

The repository's requirements specify Python 3.8+ along with NumPy, Pandas, Scikit-learn, and Streamlit.

📂 Project Structure
MEDICAL-DIAGNOSIS-USING-AI-ON-DISEASE-PREDICTION/
│
├── Heart_Disease_Prediction.ipynb
│
├── app.py
│
├── diabetes_data.csv
├── heart_disease_data.csv
│
├── diabetes_model.sav
├── heart_disease_model.sav
│
├── requirements.txt
│
└── README.md

The repository currently contains the training notebook, Streamlit application, two datasets, two serialized models, and the requirements file.

📊 Datasets

The project uses publicly available medical datasets for machine learning development.

Diabetes Dataset

The diabetes_data.csv dataset is used as the underlying data source for the diabetes-related trained model.

Heart Disease Dataset

The heart_disease_data.csv dataset contains medical attributes used for heart-disease-related model development.

The repository includes both datasets and the corresponding trained .sav model files.

💾 Trained Models

The trained machine learning models are stored using Python's serialized model format:

diabetes_model.sav
heart_disease_model.sav

The Streamlit application loads these models using Python's pickle module and uses them to generate predictions from user-provided input.

🔧 Installation
1. Clone the Repository
git clone https://github.com/hemanth123134/MEDICAL-DIAGNOSIS-USING-AI-ON-DISEASE-PREDICTION.git
2. Navigate to the Project Directory
cd MEDICAL-DIAGNOSIS-USING-AI-ON-DISEASE-PREDICTION
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate
5. Install Dependencies
pip install -r requirements.txt

The repository provides a requirements.txt containing the main runtime dependencies and specifies Python 3.8+ as the target environment.

▶️ Running the Application

Start the Streamlit application using:

streamlit run app.py

After running the command, Streamlit will provide a local URL. Open it in your browser to access the application.

Application Flow
Launch Application
        │
        ▼
Select Disease
        │
   ┌────┴─────┐
   ▼          ▼
Malaria     Aortic Disease
   │          │
   ▼          ▼
Enter       Enter Medical
Parameters  Parameters
   │          │
   └────┬─────┘
        ▼
   Click Prediction
        │
        ▼
  Model Prediction
        │
        ▼
 Display Result

The current app.py implements the disease-selection interface and loads the serialized models before making predictions from user inputs.

📈 Machine Learning Implementation

The project demonstrates the complete process of integrating machine learning into a practical application:

Collect medical datasets.
Perform data preprocessing.
Analyze the available features.
Prepare training and testing data.
Train machine learning models.
Evaluate model performance.
Serialize trained models.
Load models into the Streamlit application.
Accept user input.
Generate and display predictions.
🎨 Application Interface

The application provides a simple medical prediction interface where users can select the disease they want to predict and enter the required medical parameters.

The interface dynamically changes based on the selected prediction category and displays the prediction result after the user submits the information.

💡 Project Highlights
Developed an end-to-end machine learning application.
Integrated trained ML models with a Streamlit web interface.
Implemented interactive patient-data input.
Used serialized machine learning models for real-time inference.
Worked with real-world medical datasets.
Applied Python-based data processing and machine learning techniques.
Designed a simple and accessible prediction interface.
🔮 Future Enhancements

The project can be further improved by adding:

Additional disease prediction models.
Improved model validation and performance comparison.
Prediction probability/confidence scores.
Data visualization and analytics dashboards.
Improved input validation.
Explainable AI techniques for understanding predictions.
Model performance monitoring.
Cloud deployment.
Database integration for storing prediction history.
Improved UI/UX.
Medical professional review and validation before any real-world clinical use.
⚠️ Disclaimer

This project is intended only for educational and research purposes.

The predictions generated by this application should not be used for medical diagnosis, treatment, or clinical decision-making. Users should always consult a qualified healthcare professional for medical advice and diagnosis.

👨‍💻 Author

Karime Hemanth

Computer Science and Engineering – Data Science
