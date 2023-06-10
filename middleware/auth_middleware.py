from functools import wraps
import jwt
from flask import request
from utils.common import generate_response,token_generator
from utils.http_code import HTTP_401_UNAUTHORIZED

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("token")
        
        if not token:
            return generate_response(message="Authentication failed!", status=HTTP_401_UNAUTHORIZED)

        try:
            isValidToken = token_generator.check_token(token)

            if isValidToken == True:
                request.environ['data_token'] = token_generator.decode_token(token)
            else:
                return generate_response(message="Authentication failed!", status=HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return generate_response(message=str(e), status=HTTP_401_UNAUTHORIZED)

        # return f(data_token, *args, **kwargs)
        return f(**kwargs)

    return decorated