import time
import datetime
from server import db
from botmessage.validation import SendMessageSchema
from botmessage.models import BotMessages
from utils.http_code import HTTP_200_OK, HTTP_400_BAD_REQUEST
from utils.common import generate_response

def send_message(request, input_data):

    create_validation_schema = SendMessageSchema()
    errors = create_validation_schema.validate(input_data)

    if errors:
        return generate_response(message=errors)

    input_data['userId']   = request.environ.get('data_token')['id']
    input_data['question'] = input_data.get('message')
    input_data['answer']   = 'jawaban sementara'
    input_data['created']  = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    del input_data["message"]

    new_message = BotMessages(**input_data)
    db.session.add(new_message)
    db.session.commit()
    del input_data["userId"]
    del input_data["question"]

    return generate_response(data=input_data, message="success", status=HTTP_200_OK)

def get_message_history(request):

    message_history = BotMessages.query.filter_by(userId=request.environ.get('data_token')['id']).all()

    messages_list = [{'id': message.id, 'userId': message.userId, 'question': message.question, 'answer': message.answer, 'created': message.created} for message in message_history]

    return generate_response(data=messages_list, message="success", status=HTTP_200_OK)
    