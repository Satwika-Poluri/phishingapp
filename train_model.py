import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

print("Loading dataset...")
df = pd.read_csv('training_data.csv')

# Debugging: Print the DataFrame's shape and columns
print("DataFrame shape:", df.shape)
print("Columns in DataFrame:", df.columns.tolist())

# Check for any extra columns or formatting issues
print("First few rows of the DataFrame:")
print(df.head())

# Ensure there are no unexpected column names or spaces
df.columns = df.columns.str.strip()

print("Columns after stripping spaces:", df.columns.tolist())

print("Preparing features and labels...")
# Select only the feature columns
X = df[['length', 'dots', 'hyphens', 'ats', 'login_count', 'secure_count', 'update_count', 'bank_count', 'domain_length']]
y = df['label']

print("Features shape:", X.shape)
print("Labels shape:", y.shape)

print("Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training model...")
model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Saving model...")
joblib.dump(model, 'phishing_detector.pkl')

print("Model saved as phishing_detector.pkl")
