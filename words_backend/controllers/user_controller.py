import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.words import Words  # noqa: E501
from swagger_server import util

import json
from random import choice

with open('words_backend/words.json', 'r') as words_file:
    words = json.load(words_file)

with open('words_backend/users.json', 'r') as users_file:
    users = json.load(users_file)

with open('words_backend/user1_words.json', 'r') as user1_words_file:
    user1_words = json.load(user1_words_file)


def create_user(body):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_users_with_array_input(body):  # noqa: E501
    """Creates list of users with given input array

     # noqa: E501

    :param body: List of user object
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [User.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def create_users_with_list_input(body):  # noqa: E501
    """Creates list of users with given input array

     # noqa: E501

    :param body: List of user object
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [User.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def delete_user(username):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name that needs to be deleted
    :type username: str

    :rtype: None
    """
    return 'do some magic!'


def get_user_by_name(username):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param username: The name that needs to be fetched. Use user1 for testing.
    :type username: str

    :rtype: User
    """
    return 'do some magic!'


def get_words_to_learn(username, limit=None, status=None):  # noqa: E501
    """Get words to learn

    Returns number of words to learn # noqa: E501

    :param username: name that need to be updated
    :type username: str
    :param limit: number of words to return
    :type limit: int
    :param status: status of words to return
    :type status: List[str]

    :rtype: Words
    """

    # return 'do some BEST magic!'

    limit = 3

    # TODO(sgrade): check if needed
    # global words_learned

    # Which words the user haven't learned yet?
    words_to_learn = list()
    words_not_learned = list()
    # Words, which the user already started to learn
    for word_id, right_answers in user1_words.items():
        if right_answers < 10:
            words_to_learn.append(word_id)
        if len(words_to_learn) == limit:
            break
    if len(words_to_learn) < limit:
        words_not_learned = [str(word['id']) for word in list(words.values()) if str(word['id']) not in words_to_learn]
        while len(words_to_learn) < limit:
            candidate = choice(words_not_learned)
            if candidate not in words_to_learn:
                words_to_learn.append(candidate)

    print(words_to_learn, '\n', words_not_learned)

    # Have the user learned all the words and need to reset the learning?
    # TODO(sgrade)

    return words_to_learn


def login_user(username, password):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    return 'do some magic!'


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def mark_word_learned(username, word_id):  # noqa: E501
    """Update word status for the user

    This can only be done by the logged in user. # noqa: E501

    :param username: name that need to be updated
    :type username: str
    :param word_id: ID of word to update
    :type word_id: int

    :rtype: None
    """

    # JSON keys must be strings
    word_id_str = str(word_id)
    if word_id_str not in user1_words:
        user1_words[word_id_str] = 1
    else:
        # To prevent endless repetition counter
        if user1_words[word_id_str] == 10:
            pass
        else:
            user1_words[word_id_str] += 1

    with open('words_backend/user1_words.json', 'w') as user1_words_file:
        json.dump(user1_words, user1_words_file)

    return 'do some magic!'


def update_user(body, username):  # noqa: E501
    """Update user

    This can only be done by the logged in user. # noqa: E501

    :param body: Updated user object
    :type body: dict | bytes
    :param username: name that need to be updated
    :type username: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
