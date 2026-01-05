from flask import Flask, render_template, request

app = Flask(__name__)

def analyze_feedback(text):
    """
    Analyzes feedback using simple keyword matching.
    Returns: 'Good', 'Average', or 'Bad'
    """
    # Convert text to lowercase for case-insensitive matching
    text = text.lower()
    
    # 1. Define keywords (Simple lists)
    good_keywords = ["good", "great", "excellent", "amazing", "love", "best", "happy", "nice", "fast", "helpful"]
    bad_keywords = ["bad", "terrible", "worst", "hate", "slow", "rude", "poor", "awful", "horrible", "sad"]
    
    # 2. Initialize counters
    good_score = 0
    bad_score = 0
    
    # 3. Tokenize (split text into words)
    words = text.split()
    
    # 4. Loop through words to find matches
    for word in words:
        # Remove punctuation if attached (simple approach)
        clean_word = word.strip(".,!?")
        
        if clean_word in good_keywords:
            good_score += 1
        elif clean_word in bad_keywords:
            bad_score += 1
            
    # 5. Determine result based on scores
    if good_score > bad_score:
        return "Good"
    elif bad_score > good_score:
        return "Bad"
    else:
        return "Average"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    feedback_text = ""
    
    if request.method == 'POST':
        feedback_text = request.form.get('feedback')
        if feedback_text:
            result = analyze_feedback(feedback_text)
            
    return render_template('index.html', result=result, feedback=feedback_text)

if __name__ == '__main__':
    app.run(debug=True)
