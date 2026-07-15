# 🌊 Rising Waters – Flood Prediction System

## Overview

Rising Waters is a Machine Learning-based Flood Prediction System that predicts the likelihood of flood occurrence using historical weather and rainfall data. The application analyzes environmental parameters such as temperature, humidity, cloud cover, annual rainfall, seasonal rainfall, and regional subdivision values to determine whether flood conditions are likely.

The project follows a structured Software Development Life Cycle (SDLC) approach, documenting every phase from brainstorming and requirement analysis to development, testing, deployment, and final demonstration.

---

## Live Application

🔗 https://rising-waters-t4ig.onrender.com

---

## Key Features

- **Flood Prediction Model** – Trained Random Forest Classifier predicts flood occurrence using historical weather and rainfall data.
- **User-Friendly Interface** – Clean and responsive web interface for entering weather parameters.
- **Real-Time Prediction** – Instantly displays whether the entered conditions indicate **Flood** or **No Flood**.
- **Machine Learning Integration** – Uses a trained Scikit-Learn model (`model.pkl`) for prediction.
- **Cloud Deployment** – Publicly accessible through Render.
- **Fast Response** – Lightweight Flask backend provides quick prediction results.

---

## Tech Stack

| Layer | Technology |
|--------|------------|
| Programming Language | Python |
| Machine Learning | Scikit-Learn, Pandas, NumPy |
| Model | Random Forest Classifier |
| Backend | Flask |
| Frontend | HTML5, CSS3 |
| Deployment | Render |
| Dataset | Historical Flood & Rainfall Dataset |

---

## Repository Structure

This repository documents the complete development lifecycle of the project.

```
Rising-Waters/
│
├── 1.Brainstorming & Ideation/
│
├── 2.Requirement Analysis/
│
├── 3.Project Design Phase/
│
├── 4.Project Planning Phase/
│
├── 5.Project Development Phase/
│
├── 6.Project Testing/
│
├── 7.Project Documentation/
│
├── 8.Project Demonstration/
│
├── Demo Video.mp4
│
└── README.md
```

---

## Note

The Machine Learning model was trained using historical flood and rainfall data. The trained model is exported as **model.pkl** and integrated into a Flask web application for real-time flood prediction.

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/palemvenkatarajesh94/Rising-Waters.git
```

### Navigate to the Project

```bash
cd Rising-Waters
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Open in Browser

```
http://127.0.0.1:5000
```

---

## Input Parameters

The application accepts the following weather and rainfall parameters:

- Temperature
- Humidity
- Cloud Cover
- Annual Rainfall
- Jan–Feb Rainfall
- Mar–May Rainfall
- Jun–Sep Rainfall
- Oct–Dec Rainfall
- Average June Rainfall
- Subdivision Value

---

## Output

The trained Machine Learning model predicts one of the following outcomes:

- ✅ Flood
- ✅ No Flood

---

## Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Selection
4. Train-Test Split
5. Random Forest Model Training
6. Model Evaluation
7. Model Serialization (`model.pkl`)
8. Flask Integration
9. Web Deployment
10. Prediction

---

## Performance

The application uses a **Random Forest Classifier**, which provides reliable classification performance on the available historical flood dataset. The trained model was evaluated using a train-test split and integrated into a Flask application capable of producing real-time predictions with minimal response time.

---

## Future Enhancements

- Integration with live weather APIs
- Real-time rainfall monitoring
- GIS-based flood visualization
- Interactive charts and dashboards
- Mobile application support
- Cloud database integration
- SMS and Email flood alerts
- Multi-language support
- Advanced Machine Learning and Deep Learning models
- Early Warning Notification System

---

## Project Demonstration

**Live Demo**

🔗 https://rising-waters-t4ig.onrender.com

**GitHub Repository**

🔗 https://github.com/palemvenkatarajesh94/Rising-Waters

---

## Developed As Part of

**Skill Wallet – AI/ML Project**

**Project Title: Rising Waters – Flood Prediction System**

---

## License

This project is developed for educational and academic purposes.
