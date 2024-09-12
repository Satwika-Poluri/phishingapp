import pandas as pd

# Expanded sample data
data = {
    'url': [
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
    ],
    'length': [
        20, 25, 18, 30, 25, 28, 22, 35, 
        22, 27, 16, 31, 19, 34, 21, 27, 
        20, 30, 18, 31, 18, 32, 12, 25, 
        19, 29, 19, 24, 15, 25
    ],
    'dots': [
        2, 3, 2, 4, 2, 3, 2, 4, 
        2, 3, 2, 3, 2, 4, 2, 3, 
        2, 3, 2, 4, 2, 3, 2, 3, 
        2, 3, 2, 3, 2, 3
    ],
    'hyphens': [
        0, 1, 0, 2, 0, 1, 0, 1, 
        0, 1, 0, 1, 0, 2, 0, 1, 
        0, 1, 0, 2, 0, 1, 0, 1, 
        0, 1, 0, 1, 0, 1
    ],
    'ats': [
        0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0
    ],
    'login_count': [
        0, 1, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0
    ],
    'secure_count': [
        0, 1, 1, 0, 0, 0, 1, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0
    ],
    'update_count': [
        0, 1, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0
    ],
    'bank_count': [
        0, 1, 0, 0, 1, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0
    ],
    'domain_length': [
        12, 15, 13, 18, 9, 18, 17, 23, 
        14, 15, 15, 23, 19, 24, 17, 27, 
        17, 18, 18, 23, 18, 25, 12, 24, 
        21, 23, 21, 20, 16, 22
    ],
    'label': [
        0, 1, 0, 1, 0, 1, 0, 1, 
        0, 1, 0, 1, 0, 1, 0, 1, 
        0, 1, 0, 1, 0, 1, 0, 1, 
        0, 1, 0, 1, 0, 1
    ]
}

print("Creating DataFrame...")
df = pd.DataFrame(data)

print("Saving DataFrame to CSV...")
df.to_csv('training_data.csv', index=False)

print('training_data.csv created successfully.')
