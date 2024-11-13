import pickle
import random
import time
import pandas as pd

# Load the pre-trained model
with open('predictive_model.pkl', 'rb') as file:
    model = pickle.load(file)

def generate_sensor_data():
    """Generate random sensor data."""
    temperature = random.uniform(15.0, 45.0)
    pressure = random.uniform(900, 1100)
    humidity = random.uniform(20, 80)
    return {'temperature': temperature, 'pressure': pressure, 'humidity': humidity}

def make_decision(data):
    """Make a decision based on sensor data using the ML model."""
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    decision = "Run" if prediction == 1 else "Stop"
    return decision

# Real-time loop
print("Starting real-time analysis...")
while True:
    sensor_data = generate_sensor_data()
    decision = make_decision(sensor_data)
    print(f"Sensor Data: {sensor_data} => Decision: {decision}")
    time.sleep(3)  # Wait for 3 seconds before generating new data
