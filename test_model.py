import pandas as pd
import joblib

# Load the model
try:
    model = joblib.load('phishing_detector.pkl')
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")

# Define test data
urls = [
    'https://example.com', 'http://phishingsite.com', 'https://secure-login.com',
    'http://malicious-website.com', 'https://bank.com', 'http://fakebanking.com',
    'https://mysecureaccount.com', 'http://untrustworthy-site.com',
    'https://amazon.com', 'http://scam-site.com', 'https://paypal.com',
    'http://suspicious-link.com', 'https://github.com', 'http://fraudulent-activity.com',
    'https://microsoft.com', 'http://phishing-example.com', 'https://apple.com',
    'http://dangerous-site.com', 'https://yahoo.com', 'http://malware-site.com',
    'https://office.com', 'http://scam-example.com', 'https://zoom.us',
    'http://fake-login.com', 'https://twitter.com', 'http://deceptive-site.com',
    'https://linkedin.com', 'http://phishing-test.com', 'https://reddit.com',
    'http://baddomain.com'
]

# Define a function to extract features
def extract_features(url):
    return [
        len(url),                      # Feature 1: Length of URL
        url.count('.'),                # Feature 2: Number of dots
        url.count('-'),                # Feature 3: Number of hyphens
        url.count('@'),                # Feature 4: Number of '@' symbols
        url.lower().count('login'),    # Feature 5: Presence of 'login'
        url.lower().count('secure'),   # Feature 6: Presence of 'secure'
        url.lower().count('update'),   # Feature 7: Presence of 'update'
        url.lower().count('bank'),     # Feature 8: Presence of 'bank'
        len(url.split('/')[2])         # Feature 9: Length of the domain
    ]

# Extract features for all URLs
features = [extract_features(url) for url in urls]

# Create DataFrame with the correct column names
features_df = pd.DataFrame(features, columns=[
    'length', 'dots', 'hyphens', 'ats', 'login_count', 'secure_count',
    'update_count', 'bank_count', 'domain_length'
])

# Print DataFrame info for debugging
print("Features DataFrame:")
print(features_df.head())
print("Features DataFrame shape:", features_df.shape)
print("Features DataFrame columns:", features_df.columns.tolist())

# Make predictions
try:
    predictions = model.predict(features_df)
    for url, prediction in zip(urls, predictions):
        print(f"URL: {url}, Prediction: {'Legitimate' if prediction == 0 else 'Phishing'}")
except Exception as e:
    print(f"Error during prediction: {e}")
