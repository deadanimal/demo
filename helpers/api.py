import jwt
import time
from decouple import config

API_SECRET_KEY = 'TestData'

def create_token():
    sekarang = int(time.time())
    esok = sekarang + 86400
    payload = {'iat': sekarang,'exp': esok}
    encoded = jwt.encode(payload, API_SECRET_KEY, algorithm="HS256")
    print(encoded)

def verify_token():
    pass

def refresh_token():
    pass