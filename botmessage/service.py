import time
import datetime
from server import db
from botmessage.validation import SendMessageSchema
from botmessage.models import BotMessages
from utils.http_code import HTTP_200_OK, HTTP_400_BAD_REQUEST
from utils.common import generate_response
from tensorflow.keras.models import load_model
model = load_model('model_ai/my_model.h5')

def process_input(input_text):
    # Update this function based on how your model expects input
    # For example, if your model uses tokenized sentences, you would tokenize the input_text here
    return input_text

def generate_answer(question):
    processed_question = process_input(question)
    answer = model.predict([processed_question])[0]
    return answer

def send_message(request, input_data):

    create_validation_schema = SendMessageSchema()
    errors = create_validation_schema.validate(input_data)

    if errors:
        return generate_response(message=errors)

    input_data['userId']   = request.environ.get('data_token')['id']
    input_data['question'] = input_data.get('message')
    input_data['answer']   = generate_answer(input_data.get('message'))
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
    db.session.commit()

    messages_list = [{'id': message.id, 'userId': message.userId, 'question': message.question, 'answer': message.answer, 'created': message.created} for message in message_history]

    return generate_response(data=messages_list, message="success", status=HTTP_200_OK)
    