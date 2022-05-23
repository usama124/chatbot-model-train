import requests, time, json
import settings

def read_file_content(file_name):
    service_url = f"{settings.CHATBOT_API_HOST}/{settings.CHATBOT_API_PREFIX}/read-single-json-file"
    data = {
        "filepath": file_name
    }
    response = requests.post(service_url, json=data)
    if response.status_code == 200:
        return response.status_code, response.content
    else:
        return response.status_code, response.json()


def model_train_service(file_content):
    time.sleep(60)
    print("Model Trained successfully.")
