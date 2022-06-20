from flask import Flask, request
from flask_cors import CORS
from typingprofile import get_similar_user

APP = Flask(__name__)
CORS(APP)

typing_profiles = {}

@APP.route('/typingprofiles', methods=['POST'])
def put_typing_profile():
    response = request.get_json()
    name = response.get('name')
    user_time = response.get('userTime')
    entered_text = response.get('enteredText')

    return {
        'similar_user': get_similar_user(typing_profiles, name, user_time, entered_text)
    }

if __name__ == "__main__":
    APP.run(port=8080, debug=True)