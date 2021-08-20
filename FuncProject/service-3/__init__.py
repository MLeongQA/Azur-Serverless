import logging
import random, string
import azure.functions as func

def gen_rand_string():
    string_list = string.ascii_lowercase
    rand_string = ""
    for i in range(0,5):
        rand_string += random.choice(string_list)
    return rand_string

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(rand_string, status_code=200)
