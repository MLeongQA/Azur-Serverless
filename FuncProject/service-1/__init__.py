import logging
import requests
import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    endpoint = "https://serverless-cosmosdb.documents.azure.com:443/"
    key = "xPs1inEAPXib80m76Bgh9d5PP0lTBGJDU3bgNnqeSV3Y6nlhXysehq2th5aYTddlwlMd8JygTcx13XrXhTJE2g=="

    client = CosmosClient(endpoint, key)

    database_name = 'AzureRandDB'
    database = client.create_database_if_not_exists(id=database_name)

    container_name = 'RandomContainer'
    container = database.create_container_if_not_exists(
        id=container_name, 
        partition_key=PartitionKey(path="/username"),
        offer_throughput=400
    )

    number = requests.get("https://mikitoleongapp.azurewebsites.net/api/service-2?code=hLLFUq2d13A5tYanFsWW2jb5DPwtYwwjKIgGs1oTsqAIRkqBZXCYFA==")
    letter = requests.get("https://mikitoleongapp.azurewebsites.net/api/service-3?code=bitTeriB4DKHaEbVGn214QY0iWzZ8bXdtlSiNpEnHQxL/vdILQuY3Q==")
    
    rand_output = number.text + letter.text

    container.create_item({"id" : "id", "username": rand_output})

    return func.HttpResponse(
        rand_output,
        status_code=200
    )
    
