# Import the requests & json library to handle HTTP requests
import requests, json

def emotion_detector(text_to_analyse):
    """
    # Define a function named emotion_detector that takes a string input (text_to_analyse) 
    """
    # URL of the emotion prediction service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header) 
    
    # Format the response into json
    formatted_response = json.loads(response.text)

    # Desired Format the response into json
    final_response = formatted_response["emotionPredictions"][0]["emotion"]
    final_response['dominant_emotion'] = max(final_response, key=final_response.get)
    
    # Return the formatted response into json
    return final_response
    