Evidently AI Streamlit App (Dockerized)
This project is a Streamlit application integrated with Evidently AI for monitoring and evaluating machine learning models. The entire app is containerized using Docker for easy deployment and scaling.

🛠 Features
Upload and manage datasets
Train machine learning models
Generate interactive evaluation reports using Evidently AI
Visualize model performance and data drift
Multipage Streamlit layout
Dockerized setup for smooth deployment
🚀 Quick Start
1. Clone the Repository
git clone https://github.com/ayushgabba/Docker_project.git
cd Docker_project/evidently-ai-streamlit
2. Build the Docker Image
docker build -t evidently-streamlit-app .
3. Run the Docker Container
docker run -p 8501:8501 evidently-streamlit-app
Then open your browser and go to:
👉 http://localhost:8501

🧩 Project Structure
evidently-ai-streamlit/
├── Dockerfile
├── app.py
├── requirements.txt
├── pages/
│   ├── 1_Dataset_Upload.py
│   ├── 2_Model_Training.py
│   ├── 3_Evidently_Reports.py
│   └── 4_Prediction.py
└── README.md
app.py: Main entry point for the Streamlit app.
pages/: Contains individual pages for dataset upload, model training, Evidently AI report generation, and predictions.
Dockerfile: Instructions to containerize the application.
requirements.txt: Python dependencies.
🧪 Tech Stack
Streamlit — for the interactive web application
Evidently AI — for generating reports on model performance
Scikit-learn — for machine learning models
Docker — for containerization
Pandas, NumPy — for data manipulation
📈 Example Use Cases
Monitor ML model data drift over time
Compare model performance across different datasets
Evaluate newly trained models before deployment
⚡ Future Improvements
Integrate a database (like PostgreSQL or DynamoDB) to store uploaded datasets and models
Add user authentication and session management
Deploy to cloud platforms (AWS, Azure, GCP)
