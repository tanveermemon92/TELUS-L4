import matplotlib.pyplot as plt
import numpy as np

# Sample feature importance data
features = ['Customer Tenure', 'Number of Services', 'Interaction Patterns', 'SMS Engagement']
importance_scores = [0.35, 0.25, 0.20, 0.20]

# Plotting
plt.figure(figsize=(10, 6))
plt.barh(features, importance_scores, color='skyblue')
plt.xlabel('Importance Score')
plt.title('Feature Importance')
plt.gca().invert_yaxis()
plt.show()
