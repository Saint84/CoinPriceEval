from fastapi import FastAPI
import requests
import uvicorn

app = FastAPI()

@app.get('/')
async def get_CoinEvaluation():
    try:
        response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
        if response.status_code == 200:
            response_api = response.json()['USDBRL']
        else:
            print(response.status_code)
    except requests.HTTPError as ERROR:
        print(f'[!] {ERROR}')
    return response_api


if __name__ == '__main__':
    uvicorn.run("Main:app", 
                host="0.0.0.0", 
                port=8000, 
                log_level='info', 
                reload=True)