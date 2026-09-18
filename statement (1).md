# Project Statement

## Emotion and Sentiment Analysis Using NLTK

### 1. Problem Statement

The objective of this project is to develop a Python-based Natural Language Processing (NLP) system that can analyze a given text and identify the emotions expressed in it.

The system takes textual data as input, preprocesses the text, detects predefined emotions using an emotion-mapping file, calculates the frequency of detected emotions, and performs overall sentiment analysis using the VADER Sentiment Analyzer.

The final results are presented through console output and a graphical representation of emotion frequencies.

---

### 2. Input

The system takes text from the `read.txt` file.

Example input:

```text
I am feeling so happy, glad, and excited today!
However, yesterday I felt sad, angry, and fearful about the project.
```

---

### 3. Processing

The input text is processed through the following NLP steps:

1. Convert the text to lowercase.
2. Remove punctuation.
3. Tokenize the text into individual words.
4. Remove English stop words.
5. Perform lemmatization.
6. Match words with the emotion mappings in `emotion.txt`.
7. Calculate the frequency of each detected emotion.
8. Perform sentiment analysis using VADER.
9. Generate a bar graph representing emotion frequencies.

---

### 4. Emotion Mapping

The project uses an `emotion.txt` file to associate words with emotions.

Example:

```text
happy:happy
glad:happy
excited:happy
sad:sad
angry:anger
fearful:fear
```

---

### 5. Output

The program produces the following outputs:

* Detected Emotions List
* Emotion Frequencies
* VADER Polarity Scores
* Overall Sentiment Verdict
* Emotion Frequency Bar Graph

The overall sentiment is classified into one of three categories:

```text
Positive Sentiment
Negative Sentiment
Neutral Sentiment
```

---

### 6. Expected Result

For the given input text, the system identifies the emotions based on the mappings available in `emotion.txt` and calculates their frequency.

The program also analyzes the complete text using VADER and displays the corresponding sentiment classification.

A graph is generated to visually represent the frequency of the
