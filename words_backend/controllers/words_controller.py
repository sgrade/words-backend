import connexion
import six

from swagger_server.models.words import Words  # noqa: E501
from swagger_server import util



def find_words_by_name(term):  # noqa: E501
    """Find Words by name

    Returns all words, which have the term in their name # noqa: E501

    :param term: Term to search in the names
    :type term: str

    :rtype: List[Words]
    """
    # return 'do some magic!'

    output = list()
    for word in words:
        if term in word['name']:
            output.append(word)
    return output


def find_words_by_status(status):  # noqa: E501
    """Finds Words by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: List[str]

    :rtype: List[Words]
    """
    return 'do some magic!'


def get_words_to_learn(limit=None, status=None):  # noqa: E501
    """Get words to learn

    Returns number of words to learn # noqa: E501

    :param limit: number of words to return
    :type limit: int
    :param status: status of words to return
    :type status: List[str]

    :rtype: Words
    """
    # return 'do some BEST magic!'
    
    limit = 3

    #TODO(sgrade): check if needed
    global words_learned

    # Have the user learned all the words and need to reset the learning?
    if len(words) - len(words_learned_all[1]) < limit:
        words_learned_all[1] = list()

    # Which words the user haven't learned yet?
    words_not_learned = [word for word in words if word['name'] not in words_learned_all[1]]

    words_to_learn = list()
    while len(words_to_learn) < limit:
        candidate = choice(words_not_learned)
        if candidate not in words_to_learn:
            words_to_learn.append(candidate)

    return words_to_learn

