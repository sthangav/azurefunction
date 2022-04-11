import logging

import azure.functions as func
import pandas as pd

def main(myblob: func.InputStream):
    print("My new blob trigger")
    a = [1, 7, 2]
    myvar = pd.Series(a)
    print(myvar)
    logging.info("SSSSSSSSSSSSSSSSSSSS")
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
