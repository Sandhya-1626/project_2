# Customer Feedback Analyzer Project

## 1. Clear Problem Statement
Businesses receive a lot of customer feedback every day. Reading through every command manually to classify them as positive or negative is time-consuming and difficult to scale. There is a need for a simple automated tool that can instantly read feedback and categorize it, helping business owners understand customer sentiment quickly.

## 2. Objective of the Project
The objective is to build a beginner-friendly web application that:
- Accepts text input (customer feedback) from a user.
- Analyzes the text using basic Python string manipulation and lists (without complex machine learning models).
- Classifies the feedback into three categories: **Good**, **Average**, or **Bad**.
- Displays the result on a clean, user-friendly webpage.

## 3. Simple Working Explanation
The "AI" in this project is rule-based:
1. **Input**: The user types a sentence.
2. **Processing**: The program breaks the sentence into individual words.
3. **Analysis**: 
   - It checks how many words match a "Good Keywords" list (e.g., "amazing", "love").
   - It checks how many words match a "Bad Keywords" list (e.g., "terrible", "hate").
4. **Decision**:
   - If there are more good words, the result is **Good**.
   - If there are more bad words, the result is **Bad**.
   - If they are equal or no keywords are found, the result is **Average**.

## 4. Code Explanation (Beginner Friendly)

### Backend (`app.py`)
We use **Flask**, a lightweight Python web framework.

```python
# We define lists of words to look for
good_keywords = ["good", "great", "excellent"]
bad_keywords = ["bad", "terrible", "poor"]

# We count matches
if word in good_keywords:
    good_score += 1
```

### Frontend (`index.html`)
We use **HTML** for the structure (text box, button) and **CSS** for styling (colors, centering, shadows).

## 5. Sample Input and Output

**Scenario A:**
- **Input**: "The food was amazing and I love the service."
- **Analysis**: Finds "amazing" and "love". (Good: 2, Bad: 0)
- **Output**: **Good**

**Scenario B:**
- **Input**: "The waiting time was terrible."
- **Analysis**: Finds "terrible". (Good: 0, Bad: 1)
- **Output**: **Bad**

**Scenario C:**
- **Input**: "It was okay, not bad but not great."
- **Analysis**: Finds "bad" and "great". (Good: 1, Bad: 1)
- **Output**: **Average**

## 6. Conclusion
This project demonstrates how basic programming concepts like lists, loops, and conditional statements can be used to build a useful text analysis tool. It serves as a perfect starting point for understanding how Sentiment Analysis works before moving to advanced Machine Learning techniques.
