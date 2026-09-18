# semtiment_analysisi
# Emotion and Sentiment Analysis Using NLTK

## 📌 Project Overview

This project performs **Emotion Detection and Sentiment Analysis** on a given text using Python and Natural Language Processing (NLP).

The system processes the input text, removes unnecessary words, performs lemmatization, detects emotions using an emotion-mapping file, and analyzes the overall sentiment using **VADER Sentiment Analysis**.

Finally, the detected emotions are displayed as a frequency-based bar graph.

---

## 🎯 Objectives

The main objectives of this project are:

* To preprocess natural language text.
* To tokenize the input text into individual words.
* To remove English stop words.
* To perform lemmatization.
* To detect emotions from the input text.
* To calculate emotion frequencies.
* To perform sentiment analysis using VADER.
* To visualize detected emotions using a bar graph.

---

## 🛠️ Technologies Used

* **Python**
* **NLTK**
* **VADER Sentiment Analyzer**
* **Matplotlib**
* **Collections – Counter**

---

## 📂 Project Structure

```text
Emotion-Sentiment-Analysis/
│
├── main.py
├── read.txt
├── emotion.txt
├── graph.png
└── README.md
```

### File Description

| File          | Description                       |
| ------------- | --------------------------------- |
| `main.py`     | Main Python program               |
| `read.txt`    | Input text for analysis           |
| `emotion.txt` | Emotion-word mapping              |
| `graph.png`   | Generated emotion-frequency graph |
| `README.md`   | Project documentation             |

---

## 🔄 Working Process

The project follows these steps:

```text
Input Text
    ↓
Convert Text to Lowercase
    ↓
Remove Punctuation
    ↓
Tokenization
    ↓
Remove Stop Words
    ↓
Lemmatization
    ↓
Emotion Detection
    ↓
Emotion Frequency Calculation
    ↓
VADER Sentiment Analysis
    ↓
Generate Graph
```

---

## 🧠 How the Program Works

### 1. NLTK Resource Installation

The program automatically attempts to download the required NLTK resources such as:

* punkt
* punkt_tab
* stopwords
* wordnet
* vader_lexicon

This is handled at the beginning of the program.

### 2. Text Preprocessing

The input is read from `read.txt`.

The program:

1. Converts the text to lowercase.
2. Removes punctuation.
3. Tokenizes the text.
4. Removes stop words.
5. Performs lemmatization.

### 3. Emotion Detection

The program reads emotion mappings from `emotion.txt`.

Example:

```text
happy:happy
glad:happy
excited:happy
sad:sad
angry:anger
fearful:fear
```

The program checks whether the words from the input text occur in the emotion mapping and stores their corresponding emotions.

### 4. Emotion Frequency

The `Counter` class is used to calculate how frequently each emotion occurs.

Example output format:

```text
Detected Emotions List: [...]
Emotion Frequencies: Counter({...})
```

### 5. Sentiment Analysis

The project uses **VADER (Valence Aware Dictionary and sEntiment Reasoner)** to calculate:

* Negative score
* Neutral score
* Positive score
* Compound score

The compound score is then used to classify the overall sentiment as:

```text
Positive Sentiment
Negative Sentiment
Neutral Sentiment
```

### 6. Visualization

After detecting the emotions, Matplotlib generates a bar graph showing the frequency of each detected emotion.

The graph is saved as:

```text
graph.png
```

---

## 📥 Sample Input

The current `read.txt` contains:

```text
I am feeling so happy, glad, and excited today!
However, yesterday I felt sad, angry, and fearful about the project.
```

---

## 📤 Expected Output

When the program runs successfully, the console output will contain information similar to:

```text
Detected Emotions List: ['happy', 'happy', 'happy', 'sad', 'anger', 'fear']

Emotion Frequencies: Counter({
    'happy': 3,
    'sad': 1,
    'anger': 1,
    'fear': 1
})

VADER Polarity Scores: {
    'neg': ...,
    'neu': ...,
    'pos': ...,
    'compound': ...
}

Overall Verdict: Positive Sentiment
```

> **Note:** The exact VADER scores can vary depending on the exact input text and installed NLTK version.

---

## 📸 Output Screenshots

### Console Output

Add your actual PyCharm output screenshot here:

```text
screenshots/
└── output.png
```

Then use:

```markdown
![Console Output](screenshots/output.png)
```

### Emotion Frequency Graph

The program generates:

```text
graph.png
```

Add it to your GitHub repository and display it using:

```markdown
![Emotion Frequency Graph](graph.png)
```

---

## 📊 Sample Graph

The graph represents the number of times each emotion is detected in the input text.

For the current input and mapping, the expected emotion counts are approximately:

| Emotion | Frequency |
| ------- | --------: |
| Happy   |         3 |
| Sad     |         1 |
| Anger   |         1 |
| Fear    |         1 |

---

## ▶️ How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

Check it using:

```bash
python --version
```

### Step 2: Install Required Libraries

Open the PyCharm terminal and run:

```bash
pip install nltk matplotlib
```

### Step 3: Keep All Files in One Folder

Make sure the project contains:

```text
main.py
read.txt
emotion.txt
```

### Step 4: Run the Program

Open `main.py` in PyCharm and click:

**Run ▶**

or use:

```bash
python main.py
```

### Step 5: Check the Output

The program displays:

* Detected emotions
* Emotion frequencies
* VADER polarity scores
* Overall sentiment

It also generates:

```text
graph.png
```

---

## ✨ Features

* Automatic NLTK resource setup
* Text preprocessing
* Stop-word removal
* Lemmatization
* Emotion detection
* Emotion frequency analysis
* VADER sentiment analysis
* Graphical visualization
* Automatic creation of missing input files

---

## 🔮 Future Improvements

The project can be improved by:

* Adding a larger emotion dictionary.
* Supporting more languages.
* Creating a graphical user interface.
* Allowing users to enter text directly.
* Using machine-learning-based emotion classification.
* Adding more detailed sentiment categories.
* Creating interactive charts.
* Processing multiple text files automatically.

---

## 🎓 Learning Outcomes

Through this project, the following concepts are demonstrated:

* Natural Language Processing
* Text preprocessing
* Tokenization
* Stop-word removal
* Lemmatization
* Emotion classification
* Sentiment analysis
* Data visualization
* Python file handling
* NLTK library usage

---

## 📜 Conclusion

This project demonstrates how Natural Language Processing techniques can be combined with emotion mapping and sentiment analysis to understand the emotional content of text.

The system takes raw text as input, preprocesses it, identifies predefined emotions, calculates their frequency, and uses VADER to determine the overall sentiment. The results are also visualized through a bar graph.

---

## 👩‍💻 Author

**Saumya**

AI / ML Project

---

## 📌 Project Status

**Completed — NLP Emotion & Sentiment Analysis**
