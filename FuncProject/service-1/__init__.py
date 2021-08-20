import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    number = requests.get("https://mikitoleongapp.azurewebsites.net/api/service-2?code=hLLFUq2d13A5tYanFsWW2jb5DPwtYwwjKIgGs1oTsqAIRkqBZXCYFA==")
    letter = requests.get("https://mikitoleongapp.azurewebsites.net/api/service-2?code=hLLFUq2d13A5tYanFsWW2jb5DPwtYwwjKIgGs1oTsqAIRkqBZXCYFA==")
    
    rand_output = number.text + letter.text

    return func.HttpResponse(
        rand_output,
        status_code=200
    )
    
