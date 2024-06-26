# Customer Price Awareness Prediction
This repository contains code for developing a predictive model to identify at-risk customers who are unaware of price changes. The code includes steps for data exploration, model training, and deployment using Docker and Kubernetes.
## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Data Preparation](#data-preparation)
4. [Model Training](#model-training)
5. [Containerization](#containerization)
6. [Deployment](#deployment)
7. [Usage](#usage)
8. [Charts](#charts)

# Requirements
The following packages and dependencies are required to run the code in this repository:
1. Python 3.8+ (Lib: pandas, numpy,  matplotlib, seaborn) (Framework: Flask)
2. scikit-learn
3. PySpark
4. Docker
5. Kubernetes
6. GCP BigQuery
7. Apache Airflow

# Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/customer-awareness-prediction.git
    cd customer-awareness-prediction
    ```
2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install the required Python packages:
    ```bash
    pip install pandas numpy scikit-learn matplotlib seaborn Flask google-cloud-bigquery apache-airflow great-expectations pyspark
    ```
4. Install Docker and Kubernetes:
    - Follow the instructions to install Docker: [Docker Installation](https://docs.docker.com/get-docker/)
    - Follow the instructions to install Kubernetes: [Kubernetes Installation](https://kubernetes.io/docs/setup/)
    - Build the Docker image: docker build -t ml-model
    - Run the Docker container: docker run -p 4000:80 ml-model

# Data Preparation

Load and preprocess the data using the following code snippet:
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv('customer_data.csv')

# Preprocess data
features = ['customer_tenure', 'num_services', 'interaction_pattern', 'sms_engagement']
X = data[features]
y = data['unaware_of_price_change']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Usage 
Send a prediction request to the deployed model: curl -X POST http://<external-ip>/predict -H "Content-Type: application/json" -d '{"features": [0.5, 1, 0.8, 0.3]}'

# Contribution
Contributions are welcome! Please feel free to submit pull requests or open issues for any improvements or bug fixes.
Make sure to replace `your-username` and `your-repository` with your actual GitHub username and repository name. Additionally, include a `LICENSE` file in your repository with the appropriate license text.

# License
This project is licensed under the MIT License.
