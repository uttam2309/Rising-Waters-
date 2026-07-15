import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_excel("flood dataset.xlsx")

# Features
X = df.drop("flood", axis=1)

# Target
y = df["flood"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, pred)

print("Model Accuracy:", accuracy)

# Save Model
joblib.dump(model, "model.pkl")

print("Model saved successfully as model.pkl")