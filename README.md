Project overview
This script connects to a Telegram channel using Telethon and a bot token, reads recent messages, classifies them as “Scam” or “Not Scam” with a TF‑IDF + Multinomial Naive Bayes text model, and posts an alert message for any detected scams. It also evaluates the model using cross‑validation and prints a classification report on the small synthetic dataset.​

Features
Connects to a Telegram channel via Telethon client and a bot token using provided api_id, api_hash, and channel URL.​

Trains a simple TF‑IDF + MultinomialNB text classifier on a manually curated dataset of scam and non‑scam example texts.​

Monitors up to the last 100 messages from the channel, classifies each, and sends an alert to channel_id for messages predicted as “Scam”.​

Requirements
Python 3.8+

Libraries: telethon, python-telegram-bot (or telegram), scikit-learn, pandas, nltk, and time.​

NLTK English stopwords are downloaded at runtime using nltk.download('stopwords').​

Install the dependencies:

bash
pip install telethon python-telegram-bot scikit-learn pandas nltk
How it works
A small labeled dataset (data) of scam and non‑scam text examples is defined and split into texts and labels.​

A scikit‑learn pipeline with TfidfVectorizer (using NLTK English stopwords) and MultinomialNB is created and trained on this dataset.​

classify_message(message_text) returns "Scam" or "Not Scam" based on the model’s prediction.​

monitor_channel() asynchronously iterates over recent messages from the target channel and calls send_alert() for each message classified as scam, then sleeps briefly to avoid spamming.​

Usage
Replace api_id, api_hash, bot_token, channel, and channel_id in the script with your own Telegram API and bot credentials.​

Run the script once to create the Telethon session and start the monitoring loop:

bash
python Telegram.py
Keep the script running on a server or local machine; it will read recent messages and push alerts to your specified channel whenever potential scam content is detected.​

Notes and improvements
Current training data is very small and synthetic; for production use, expand the dataset with real labeled examples to improve accuracy.​

Some model‑building code is duplicated at the bottom of the file; refactoring into reusable functions or a class would make maintenance easier.​

Consider storing secrets (api_id, api_hash, bot_token) in environment variables or a config file instead of hard‑coding them to protect credentials.
