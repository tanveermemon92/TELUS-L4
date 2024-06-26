# Customer Price Awareness Prediction
# Overview
This repository contains code for developing a predictive model to identify at-risk customers who are unaware of price changes. The code includes steps for data exploration, model training, and deployment using Docker and Kubernetes.

# Requirements
The following packages and dependencies are required to run the code in this repository:
Python 3.8+
pandas
numpy
scikit-learn
matplotlib
seaborn
Flask
Docker
Kubernetes
Google Cloud Platform (GCP) BigQuery
Apache Airflow
Great Expectations
PySpark

# Installation
1. Clone the repository: git clone https://github.com/tanveermemon92/TELUS-L4
2. Create a virtual environment and activate it: python -m venv venv
source venv/bin/activate
3. Install the required Python packages: pip install pandas numpy scikit-learn matplotlib seaborn Flask google-cloud-bigquery apache-airflow great-expectations pyspark
4. Install Docker and Kubernetes:
# Build the Docker image
docker build -t ml-model
# Run the Docker container
docker run -p 4000:80 ml-model

# Usage
Send a prediction request to the deployed model: curl -X POST http://<external-ip>/predict -H "Content-Type: application/json" -d '{"features": [0.5, 1, 0.8, 0.3]}'

# Contribution
Contributions are welcome! Please feel free to submit pull requests or open issues for any improvements or bug fixes.
Make sure to replace `your-username` and `your-repository` with your actual GitHub username and repository name. Additionally, include a `LICENSE` file in your repository with the appropriate license text.

# License
This project is licensed under the MIT License.
