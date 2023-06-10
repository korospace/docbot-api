from flask import Response
from flask_restful import Resource
from flask import request, make_response
from middleware.auth_middleware import token_required
from botmessage.service import send_message, get_message_history

class Message(Resource):
    @token_required
    @staticmethod
    def post() -> Response:
        """
        POST response method for send message to bot.

        :return: JSON object
        """
        input_data = request.form.to_dict()

        response, status = send_message(request, input_data)
        return make_response(response, status)

    @token_required
    @staticmethod
    def get() -> Response:
        """
        GET response method for listing message history with bot.

        :return: JSON object
        """
        response, status = get_message_history(request)
        return make_response(response, status)