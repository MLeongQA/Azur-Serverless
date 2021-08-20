import logging
import random
import azure.functions as func

def gen_rand_num():
    rand_num = ""
    for i in range(0, 5):
        rand_num += str(random.randint(1,9))
    return rand_num 

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(gen_rand_num(), status_code=200)
