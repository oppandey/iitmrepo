import pandas as pd
import random

# Example ham and spam messages
ham_examples = [
    "Hey, are we still meeting today?",
    "I'll call you later.",
    "Don't forget to bring your notebook.",
    "See you at the office.",
    "Happy birthday! Have a great day.",
    "Can you send me the report?",
    "Let's catch up soon.",
    "Meeting is postponed to tomorrow.",
    "Lunch at 1 PM?",
    "Good morning! How are you?"
]

spam_examples = [
    "Congratulations! You've won a $1000 gift card. Click here to claim.",
    "URGENT! Your account has been compromised. Reply to secure.",
    "You have been selected for a free vacation. Call now!",
    "Win a brand new car! Text WIN to 12345.",
    "Get cheap loans now. No credit check required.",
    "Exclusive offer! Buy 1 get 1 free. Limited time only.",
    "You are a lucky winner! Claim your prize.",
    "Earn money from home. No experience needed.",
    "Your mobile number has won $500,000.",
    "Act now! Offer expires soon."
]

# Generate 1000 rows with 80% ham, 20% spam
data = []
for _ in range(800):
    data.append(['ham', random.choice(ham_examples)])
for _ in range(200):
    data.append(['spam', random.choice(spam_examples)])

random.shuffle(data)

df = pd.DataFrame(data, columns=['v1', 'v2'])
df.to_csv('sms_spam_dataset.csv', index=False)