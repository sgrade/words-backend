import connexion
import six

from swagger_server.models.word import Word  # noqa: E501
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


def find_words_by_name(term):  # noqa: E501
    """Find Words by name

    Returns all words, which have the term in their name # noqa: E501

    :param term: Term to search in the names
    :type term: str

    :rtype: List[Words]
    """
    return 'do some magic!'


def find_words_by_status(status):  # noqa: E501
    """Finds Words by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: List[str]

    :rtype: List[Words]
    """
    return 'do some magic!'


def get_words(limit=None, status=None):  # noqa: E501
    """Get words to learn

    Returns number of words to learn # noqa: E501

    :param limit: number of words to return
    :type limit: int
    :param status: status of words to return
    :type status: List[str]

    :rtype: Words
    """
    limit = 3

    # TODO(sgrade): check if needed
    # global words_learned

    # Which words the user haven't learned yet?
    word_ids_to_learn = list()
    words_not_learned = list()
    
    word_ids = list(words.keys())

    # Looking for word IDs to learn
    # All words
    while len(word_ids_to_learn) < limit:
        id = choice(word_ids)

        # Words, which the user already started to learn
        if id in user1_words.keys():
            # Number or right answers
            if user1_words[id] < 10:
                word_ids_to_learn.append(id)
        # This word we haven't started yet
        else:
            word_ids_to_learn.append(id)
        
    words_to_learn = list()
    for word_id in word_ids_to_learn:
        words_to_learn.append(words[word_id])

    # Have the user learned all the words and need to reset the learning?
    # TODO(sgrade)

    return words_to_learn


def mark_word_learned(body):  # noqa: E501
    """Update word status for the user

    This can only be done by the logged in user. # noqa: E501

    :param body: Word object
    :type body: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        body = Word.from_dict(connexion.request.get_json())  # noqa: E501

        word_id = body.id
        print(word_id)

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

        # Writing to file doesn't work on GCP
        # OSError: [Errno 30] Read-only file system: 'words_backend/user1_words.json'
        # with open('words_backend/user1_words.json', 'w') as user1_words_file:
        #     json.dump(user1_words, user1_words_file)

        print(user1_words)
        return True

    return False
