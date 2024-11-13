import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Generate a random dataset (temperature, pressure, humidity, and label)
data = {
    'temperature': [random.uniform(15.0, 45.0) for _ in range(500)],
    'pressure': [random.uniform(900, 1100) for _ in range(500)],
    'humidity': [random.uniform(20, 80) for _ in range(500)],
    'should_run': [random.choice([0, 1]) for _ in range(500)]  # 0 for "stop", 1 for "run"
}

df = pd.DataFrame(data)

# Split data
X = df[['temperature', 'pressure', 'humidity']]
y = df['should_run']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model to a file
with open('predictive_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as 'predictive_model.pkl'")
