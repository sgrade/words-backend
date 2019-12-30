import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.word import Word  # noqa: E501
from swagger_server import util


def add_word(body):  # noqa: E501
    """Add a new word to the store

     # noqa: E501

    :param body: Word object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Word.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_word(word_id, api_key=None):  # noqa: E501
    """Deletes a word

     # noqa: E501

    :param word_id: Word id to delete
    :type word_id: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_word_by_id(word_id):  # noqa: E501
    """Find word by ID

    Returns a single word # noqa: E501

    :param word_id: ID of word to return
    :type word_id: int

    :rtype: Word
    """
    return 'do some magic!'


def update_word(body):  # noqa: E501
    """Update an existing word

     # noqa: E501

    :param body: Word object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Word.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_word_with_form(word_id, name=None, status=None):  # noqa: E501
    """Updates a word in the store with form data

     # noqa: E501

    :param word_id: ID of word that needs to be updated
    :type word_id: int
    :param name: 
    :type name: str
    :param status: 
    :type status: str

    :rtype: None
    """
    return 'do some magic!'


def upload_file(word_id, body=None):  # noqa: E501
    """uploads an image

     # noqa: E501

    :param word_id: ID of word to update
    :type word_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        body = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
