import connexion
import six

from swagger_server.models.word import Word  # noqa: E501
from swagger_server.models.words import Words  # noqa: E501
from swagger_server import util


def find_words_by_name(term):  # noqa: E501
    """Find Words by name

    Returns all words, which have the term in their name # noqa: E501

    :param term: Term to search in the names
    :type term: str

    :rtype: List[Word]
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
    return 'do some magic!'


def mark_word_learned(body):  # noqa: E501
    """Update word status for the user

    This can only be done by the logged in user. # noqa: E501

    :param body: Word object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Word.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
