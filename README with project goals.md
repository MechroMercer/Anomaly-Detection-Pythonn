# Anomaly Detection App

A lightweight and interactive anomaly detection tool powered by Python.  
Upload your dataset, select detection algorithms, customize parameters, and visualize anomalies.  

---
## 🎯 Project Goals

This application is designed to detect anomalies in datasets using machine learning algorithms. It aims to support in identifying irregular patterns that may indicate errors, fraud, or unusual behavior.

### Key Features
- ** Data Import and Preprocessing**  
  Supports CSV, Excel, and JSON formats. Includes tools for data cleaning and transformation using `pandas`.

- ** Anomaly Detection Algorithms**  
  Includes multiple algorithms (k-Nearest Neighbors, Isolation Forest, One-Class SVM) via `scikit-learn` and `pyod`. Users can configure algorithm parameters.

- ** Data Visualization**  
  Visualize datasets and anomalies using `matplotlib`, `seaborn`, or `plotly`.

- ** Notifications**  
  Configurable alerts for detected anomalies via email or internal app notifications using `notifiers`.

- ** User Interface**  
  Built with `Streamlit` for a simple, intuitive experience.

-Below is a basic plan of development some actions may differ in the final version

### "Week" 1 – Setup & Data Import
- Initialize GitHub repo & README
- Project folder structure
- File import system (CSV, Excel, JSON)
- Streamlit upload interface
- Data cleaning functions
- First commit with working file preview

### "Week" 2 – Anomaly Detection
- Integrate ML algorithms via `scikit-learn` / `pyod`
- Create selection interface for models & parameters
- Generate anomaly flags
- Export results
- Logging system for analysis steps

### "Week" 3 – Visualization & Alerts
- Choose visualization tools
- Create visual reports (scatter, boxplot, etc.)
- Build basic email alert system
- Configurable alert thresholds

### "Week" 4 – Final Touches
- Clean up UI
- Save model config options
- Final testing with sample datasets
- Publish & document results

---

