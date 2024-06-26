# Customer Price Awareness Prediction
This repository contains code for developing a predictive model to identify at-risk customers who are unaware of price changes. The code includes steps for data exploration, model training, and deployment using Docker and Kubernetes.
## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contribution](#contribution)
5. [License](#license)
## Requirements
The following packages and dependencies are required to run the code in this repository:
1. Python 3.8+ (Lib: pandas, numpy,  matplotlib, seaborn) (Framework: Flask)
2. scikit-learn
3. PySpark
4. Docker
5. Kubernetes
6. GCP BigQuery
7. Apache Airflow
## Installation
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
# Usage
Send a prediction request to the deployed model: curl -X POST http://<external-ip>/predict -H "Content-Type: application/json" -d '{"features": [0.5, 1, 0.8, 0.3]}'
# Contribution
Contributions are welcome! Please feel free to submit pull requests or open issues for any improvements or bug fixes.
Make sure to replace `your-username` and `your-repository` with your actual GitHub username and repository name. Additionally, include a `LICENSE` file in your repository with the appropriate license text.
# License
This project is licensed under the MIT License.
