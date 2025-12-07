import time
from telethon.sync import TelegramClient
from telegram import Bot
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import nltk
import pandas as pd

nltk.download('stopwords')

scam_keywords = ['bitcoin', 'crypto', 'investment opportunity', 'fast return', 'double your money', 'risk-free', 'guaranteed profits']

api_id = '28321707' 
api_hash = 'f90bd70d78bc6754fcf7ba101b8961f8' 
channel = 'https://t.me/example_channel2805'  

bot_token = '7696851236:AAGVdvernkefJ1ip44enCYwfePcmCuKp_GQ'
channel_id = '@example_channel2805' 

bot = Bot(token=bot_token)

client = TelegramClient('session_name', api_id, api_hash)

data = [
    ('Bitcoin investment opportunity, guaranteed return!', 1),
    ('Buy now, get 2x returns, no risk involved!', 1),
    ('Click here to earn fast money!', 1),
    ('Exclusive cryptocurrency investment!', 1),
    ('This is your last chance to double your money!', 1),
    ('Invest in our crypto coin today for big returns!', 1),
    ('Limited-time offer to get rich quick with no risk!', 1),
    ('Guaranteed investment opportunity, don’t miss out!', 1),
    
    ('Latest news in technology!', 0),
    ('How to improve your personal health', 0),
    ('Join our community for free health tips!', 0),
    ('Best practices for improving productivity in 2024', 0),
    ('Top 10 tips for achieving your fitness goals', 0),
    ('New software update brings amazing features!', 0),
    ('How to start your own small business successfully', 0),
    ('Understanding digital marketing strategies for 2024', 0)
]


texts, labels = zip(*data)

model = make_pipeline(TfidfVectorizer(stop_words=nltk.corpus.stopwords.words('english')), MultinomialNB())

model.fit(texts, labels)

def classify_message(message_text):
    return "Scam" if model.predict([message_text])[0] == 1 else "Not Scam"

def send_alert(message_text):
    alert_message = f"🚨 Potential Scam Detected: {message_text}"
    try:
        bot.send_message(chat_id=channel_id, text=alert_message)
        print(f"Alert sent to channel: {alert_message}")
    except Exception as e:
        print(f"Error sending alert: {e}")

async def monitor_channel():
    async for message in client.iter_messages(channel, limit=100):  
        if message.text:
            result = classify_message(message.text)
            print(f"Message: {message.text}\nClassification: {result}")
            if result == "Scam":
                send_alert(message.text)
            time.sleep(1)

with client:
    client.loop.run_until_complete(monitor_channel())
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import nltk

nltk.download('stopwords')

texts, labels = zip(*data)

model = make_pipeline(TfidfVectorizer(stop_words=nltk.corpus.stopwords.words('english')), MultinomialNB())

model.fit(texts, labels)

def classify_message(message_text):
    return "Scam" if model.predict([message_text])[0] == 1 else "Not Scam"

from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report

cv_scores = cross_val_score(model, texts, labels, cv=5, scoring='accuracy')
print(f"Cross-validation scores: {cv_scores}")
print(f"Average accuracy: {cv_scores.mean()}")

predictions = model.predict(texts)
print(classification_report(labels, predictions))
