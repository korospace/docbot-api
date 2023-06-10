from flask_restful import Api
from botmessage.views import Message

def create_botmessage_routes(api: Api):
    """Adds resources to the api.
    :param api: Flask-RESTful Api Object
    """
    api.add_resource(Message, "/api/botmessage/message/")
