# feature_extraction.py

def extract_features(url):
    # Example feature extraction logic
    features = {
        len(url),                      # Feature 1: Length of URL
        url.count('.'),                # Feature 2: Number of dots
        url.count('-'),                # Feature 3: Number of hyphens
        url.count('@'),                # Feature 4: Number of '@' symbols
        url.lower().count('login'),    # Feature 5: Presence of 'login'
        url.lower().count('secure'),   # Feature 6: Presence of 'secure'
        url.lower().count('update'),   # Feature 7: Presence of 'update'
        url.lower().count('bank'),     # Feature 8: Presence of 'bank'
        len(url.split('/')[2])         # Feature 9: Length of the domain
    }
    return features

