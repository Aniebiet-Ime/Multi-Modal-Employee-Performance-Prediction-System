# Multi-Modal Employee Performance Prediction System

## Project Overview
This is a Machine Learning Capstone Project for the **Applied Machine Learning** course. The system aims to build a comprehensive employee performance prediction tool that integrates insights from three distinct data modalities:
1.  **Structured Quantitative Metrics**: (e.g., tasks completed, quality ratings, satisfied clients).
2.  **Behavioral Performance Indicators**: (e.g., meeting attendance, collaboration, punctuality).
3.  **Audio-Based Communication Features**: (e.g., speech sentiment, energy levels, clarity).

The project involves processing 5,000 employee records across interconnected data sources to extract maximum predictive power using supervised learning, feature engineering, and ensemble methods.

## Team Members and Roles

The project is developed by a three-member team, with specific leadership assigned to the core technical phases:

| Team Member | Primary Role | Phase Lead |
| :--- | :--- | :--- |
| **Aniebietabasi Ime** | Lead Data Scientist & Project Coordinator | **Phase 3**: Ensemble Model Building & Optimization |
| **Semfon Essien** | Data Integration Specialist | **Phase 2**: Feature Engineering & Data Fusion |
| **Sunday Boniface** | Machine Learning Researcher | **Phase 1**: Individual Model Development |

### Collaboration
While each member leads a specific phase, the entire team collaborates on:
*   **Phase 4**: Comprehensive Analysis and Business Insights Report.
*   Overall project documentation and technical verification.

## Project Structure (4 Phases)
1.  **Phase 1: Individual Model Development**: Developing baseline models for each data source (Structured, Behavioral, Audio).
2.  **Phase 2: Feature Engineering and Data Fusion**: Intelligently combining data sources to create a unified feature set.
3.  **Phase 3: Ensemble Model Building and Optimization**: Implementing advanced ensemble methods to improve prediction accuracy.
4.  **Phase 4: Analysis and Insights**: Communicating technical findings to business stakeholders and providing actionable HR insights.

## Dataset Description
The system leverages 5,000 employee records across three interconnected CSV files located in the `February 2026` directory:

### 1. Structured Quantitative Metrics (`structured_data.csv`)
*Target Variable: performance_rating (High, Medium, Low)*
*   `employee_id`: Unique identifier (1001-6000)
*   `tasks_completed`: Total tasks finished
*   `average_task_quality`: Quality rating (1-10)
*   `projects_led`: Number of projects managed
*   `client_satisfaction_score`: Feedback (0-100)
*   `hours_worked`: Total effort hours
*   `deadline_met_score`: Adherence rating (1-10)
*   `innovation_score`: Creativity rating (1-10)
*   `efficiency_score`: Work speed rating (1-10)

### 2. Behavioral Performance Indicators (`behavior_logs.csv`)
*Target Variable: performance_rating*
*   `meetings_attended`: Participation count
*   `collaboration_score`: Teamwork rating (1-10)
*   `punctuality_score`: Timeliness rating (1-10)
*   `training_hours_completed`: Skill investment
*   `work_engagement_score`: Engagement rating (1-10)
*   `peer_interaction_score`: Colleague quality (1-10)
*   `initiative_score`: Proactiveness rating (1-10)
*   `task_followup_score`: Follow-through rating (1-10)

### 3. Audio Communication Features (`audio_features.csv`)
*Target Variable: performance_rating*
*   `speech_sentiment_score`: Tone sentiment (-1 to 1)
*   `speech_energy_level`: Voice energy (1-10)
*   `speech_clarity_score`: Communication clarity (1-10)
*   `tone_consistency_score`: Tone stability (1-10)
*   *(Note: Additional features include pacing, pause frequency, and vocal variety as per data modality)*

## Getting Started
To initialize the project environment and boilerplate code:
1.  Ensure you are on a Windows machine.
2.  Run the setup script:
    ```powershell
    .\setup_project.bat
    ```
3.  This will create the `src` directory containing the class signatures for each team member.
4.  Verify the setup:
    ```powershell
    python src\main.py
    ```

## Technologies Used
*   **Language**: Python
*   **Libraries**: Scikit-learn, Pandas, NumPy, Matplotlib/Seaborn.
*   **Techniques**: Regression, Classification, Feature Engineering, Ensemble Learning (Stacking/Voting).

---
*Developed as part of the Applied Machine Learning Capstone Project - 2026*
