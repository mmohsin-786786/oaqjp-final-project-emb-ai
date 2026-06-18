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
    
    # If the response status code is 200, extract the dictionary values from the response
    if response.status_code == 200:
        # Format the response into json
        formatted_response = json.loads(response.text)
        # Desired Format the response into json
        final_response = formatted_response["emotionPredictions"][0]["emotion"]
        final_response['dominant_emotion'] = max(final_response, key=final_response.get)
        anger = final_response['anger']
        disgust = final_response['disgust']
        fear = final_response['fear']
        joy = final_response['joy']
        sadness = final_response['sadness']
        dominant_emotion = final_response['dominant_emotion']
    
    # If the response status code is 500 or 400, set dictionary values to None
    elif response.status_code in [400, 500]:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None
    
    # For any other unexpected status codes, set dictionary values to None
    else:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None

    # Return the formatted response into json
    return {"anger": anger,"disgust": disgust,"fear": fear,"joy": joy,"sadness": sadness,"dominant_emotion": dominant_emotion}
    
    
    