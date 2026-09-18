import os
import string
from collections import Counter
import matplotlib.pyplot as plt

import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# --- Step 1: Download Required NLTK Packages Automatically ---
required_nltk_resources = ['punkt', 'punkt_tab', 'stopwords', 'wordnet', 'vader_lexicon']
for resource in required_nltk_resources:
    nltk.download(resource, quiet=True)

# --- Step 2: Ensure Input Files Exist (Fallback Creation) ---
if not os.path.exists('read.txt'):
    with open('read.txt', 'w', encoding='utf-8') as f:
        f.write("I love working on artificial intelligence! It makes me feel happy, excited, and safe.")

if not os.path.exists('emotions.txt'):
    default_emotions = (
        "happy:happy\nexcited:happy\nlove:happy\nsafe:happy\n"
        "sad:sad\nfearful:fear\nangry:anger\n"
    )
    with open('emotions.txt', 'w', encoding='utf-8') as f:
        f.write(default_emotions)

# --- Step 3: Text Preprocessing ---
text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

tokenized_words = word_tokenize(cleaned_text, "english")

# Remove stop words
stop_words = set(stopwords.words('english'))
final_words = [word for word in tokenized_words if word not in stop_words]

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemma_words = [lemmatizer.lemmatize(word) for word in final_words]

# --- Step 4: Emotion Mapping ---
emotion_list = []
with open('emotions.txt', 'r', encoding='utf-8') as file:
    for line in file:
        clear_line = line.strip()
        if ':' not in clear_line:
            continue
        word, emotion = clear_line.split(':', 1)
        if word.strip() in lemma_words:
            emotion_list.append(emotion.strip())

print("Detected Emotions List:", emotion_list)
w = Counter(emotion_list)
print("Emotion Frequencies:", w)

# --- Step 5: VADER Sentiment Analysis ---
def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print("\nVADER Polarity Scores:", score)
    if score['compound'] >= 0.05:
        print("Overall Verdict: Positive Sentiment")
    elif score['compound'] <= -0.05:
        print("Overall Verdict: Negative Sentiment")
    else:
        print("Overall Verdict: Neutral Sentiment")

sentiment_analyse(cleaned_text)

# --- Step 6: Plotting & Visualization ---
if w:
    fig, ax1 = plt.subplots()
    ax1.bar(w.keys(), w.values())
    fig.autofmt_xdate()
    plt.savefig('graph.png')
    plt.show()
else:
    print("\nNo matching emotions found in emotions.txt to plot.")