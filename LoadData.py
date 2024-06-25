import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset (sample data)
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
