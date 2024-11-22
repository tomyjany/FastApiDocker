from typing import Union
import json
import requests
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Service": "subbing"}

@app.post("/squaredplus/{item}")
def operation(item: int):
    post_data = {"item": item}
    # response = requests.post('http://localhost:8090/test', data=int(item), timeout=10)
    response = requests.post(f'http://square:8090/test/{item}', timeout=10)
    if response.status_code != 200:
        print('Request failed with status code:', response.status_code)
        print('Response:', response.text)
        return {"error": "ERROR CALLING OCR ENDPOINT"}
    data = response.json()
    return {"custom_function": data['item_squared']+1}
    print(data)
    return {"success": "happy"}

    


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
