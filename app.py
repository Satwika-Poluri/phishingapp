from flask import Flask, request, jsonify,render_template
import pandas as pd

import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('phishing_detector.pkl')

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

# Define the route for the homepage
@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/analyze-url', methods=['POST'])
def analyze_url():
    try:
        data = request.get_json()
        if 'url' not in data:
            raise ValueError("URL not found in request")

        url = data['url']

        # Extract features from the URL
        features = extract_features(url)

        # Convert features to a DataFrame with the correct column names
        features_df = pd.DataFrame([features], columns=[
            'length', 'dots', 'hyphens', 'ats', 'login_count', 'secure_count',
            'update_count', 'bank_count', 'domain_length'
        ])

        # Predict whether the URL is phishing or legitimate
        result = model.predict(features_df)[0]

        # Convert result to a readable format
        result_text = 'Phishing' if result == 1 else 'Legitimate'

        return jsonify({'url': url, 'result': result_text})
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500



@app.route('/test', methods=['GET'])
def test():
    return "Flask is working!"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
