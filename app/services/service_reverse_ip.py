from decouple import config
from fastapi.responses import JSONResponse
import requests

class ReverseIPService:
    def __init__(self):
        self.api_key = config("API_KEY")

    def get_lookup(self, ip_address):
        url = f'http://api.ipapi.com/{ip_address}?access_key={self.api_key}'

        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                return JSONResponse(status_code=404, content={"message": 'Resource not found'})
        except:
            return JSONResponse(status_code=422, content={"message": "Invalid format"})