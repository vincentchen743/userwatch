from flask import Flask, request
from flask_cors import CORS
import json

APP = Flask(__name__)
CORS(APP)

typing_profiles = {}

@APP.route('/typingprofiles', methods=['POST'])
def put_typing_profile():
    response = request.get_json()
    name = response.get('name')
    user_time = response.get('userTime')
    entered_text = response.get('enteredText')

    time_between_keys = []
    for i in range(1, len(user_time)):
        time_between_keys.append((entered_text[i - 1] + entered_text[i], user_time[i] - user_time[i - 1]))
    typing_profiles[name] = dict(time_between_keys)

    similarity = {}

    # for each key pair for this user,
    # compare to other users & see if they have this key
    # if they do, then compare the timings
    # get the closest timing and save it
    for k, v in typing_profiles[name].items():
        closest_time = float('inf')
        closest_user = 'none'
        all_other_users = list(typing_profiles.keys())
        all_other_users.remove(name)
        for user in all_other_users:
            # print(f'comparing keypair {k} with {user}')
            if k in typing_profiles[user]:
                if abs(typing_profiles[user][k] - v) < closest_time:
                    closest_time = abs(typing_profiles[user][k] - v)
                    closest_user = user
                    # print(f'new closest time is now {closest_time} and user is now {closest_user}')
        if closest_user != 'none':
            if closest_user not in similarity:
                similarity[closest_user] = 1
            else:
                similarity[closest_user] += 1
    sorted_similarities = list(similarity.items())
    sorted_similarities.sort(key=lambda x: x[1], reverse=True)
    # print(sorted_similarities)
    if len(typing_profiles) == 1 or len(sorted_similarities) == 0:
        return {'similar_user': 'no one'}
    return json.dumps({
        'similar_user': sorted_similarities[0][0]
    })

@APP.route('/similar', methods=['GET'])
def get_most_similar():
    pass

if __name__ == "__main__":
    APP.run(port=8080, debug=True)