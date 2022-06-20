def generate_typing_profile(typing_profiles, name, user_time, entered_text):
    '''
    generate_typing_profile
    Helper function to create keypair timings for a given user
    '''
    time_between_keys = []
    for i in range(1, len(user_time)):
        time_between_keys.append((entered_text[i - 1] + entered_text[i], user_time[i] - user_time[i - 1]))
    typing_profiles[name] = dict(time_between_keys)
    return typing_profiles

def get_similar_user(typing_profiles, name, user_time, entered_text):
    '''
    get_similar_user
    This function returns the most similar typing for a given user
    by comparing each keypair typed to other users and comparing the timings between keypairs
    A closest user is defined for each keypair
    Returns:
        - 'no one' if first user or no similar users
        - user name of whoever is most similar
    '''
    typing_profiles = generate_typing_profile(typing_profiles, name, user_time, entered_text)
    similarity = {}

    for k, v in typing_profiles[name].items():
        closest_time = float('inf')
        closest_user = 'none'
        all_other_users = list(typing_profiles.keys())
        all_other_users.remove(name)
        for user in all_other_users:
            if k in typing_profiles[user]:
                if abs(typing_profiles[user][k] - v) < closest_time:
                    closest_time = abs(typing_profiles[user][k] - v)
                    closest_user = user
        if closest_user != 'none':
            if closest_user not in similarity:
                similarity[closest_user] = 1
            else:
                similarity[closest_user] += 1
    sorted_similarities = list(similarity.items())
    sorted_similarities.sort(key=lambda x: x[1], reverse=True)
    if len(typing_profiles) == 1 or len(sorted_similarities) == 0:
        return 'no one'
    return sorted_similarities[0][0]
