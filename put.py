import boto3
import json
import time
import os
from datetime import datetime
from random import randint
from dotenv import load_dotenv
load_dotenv()

my_stream_name = 'test-stream'

client = boto3.client('kinesis', region_name=os.getenv('AWS_DEFAULT_REGION'), aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY_ID'))

def put_to_stream(temp, humi, co2, pres ,timestamp ,devi):
    payload = {
        "result": "success",
        "error_code": "0",
        "device_id": devi,
           "coord": {
                "lon": "-8.61",
                "lat": "41.15"
              },
        "server_time": timestamp,
        "temperature": temp,
        "pressure": pres,
        "humidity": humi,
        "co2": co2,
    }

    put_response = client.put_record(
                    StreamName=my_stream_name,
                    Data=json.dumps(payload),
                    PartitionKey=devi)
    return put_response

while True:
    devi = '39278391'
    temp = randint(0, 40)
    humi = randint(0, 40)
    pres = randint(0, 40)
    co2  = randint(0, 40)
    timestamp = time.time()

    result = put_to_stream(temp, humi, co2, pres ,timestamp ,devi)

    time.sleep(10)
    print('response: {}'.format(result))