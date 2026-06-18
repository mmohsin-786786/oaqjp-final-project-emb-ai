# Import the relevant libraries and functions
from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")

# Define the function
@app.route("/emotionDetector")
def sent_analyzer(): 
    
    # Retrieve the text to analyze from the request arguments 
    text_to_analyze = request.args.get('textToAnalyze')
    
    if not text_to_analyze or text_to_analyze.strip() == "":
       return "Invalid text! Please try again!."
    
    # Pass the text to the sentiment_analyzer function and store the response 
    response = emotion_detector(text_to_analyze)

    # Extract the value of dominant_emotion
    dominant_emotion = response['dominant_emotion']
    
    # Check if the label is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid input! Try again."
    else:
    #Return a formatted string with the sentiment label and score
        return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

# Render the HTML template using render_index_page
@app.route("/")
def render_index_page():
    return render_template('index.html')

# Run the application on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)