import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.word import Word  # noqa: E501
from swagger_server import util

import config


def create_word(body=None):  # noqa: E501
    """Create a new word in the database

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Word.from_dict(connexion.request.get_json())  # noqa: E501
    
    # Reference for new document in Words collection
    doc_ref = config.words_ref.document()  
    # ID of the document to be the Word ID
    body.id = doc_ref.id
    
    # Create dictionary from the instance of Word class
    body_dict = dict()
    for attribute in body.attribute_map:
        body_dict[attribute] = getattr(body, attribute)
    
    # Writing to the document
    doc_ref.set(body_dict)
    
    # print(doc_ref.get().to_dict())
    
    return True


def delete_word(word_id, api_key=None):  # noqa: E501
    """Delete word

     # noqa: E501

    :param word_id: Word id to delete
    :type word_id: str
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_word_by_id(word_id):  # noqa: E501
    """Find word by ID

    Returns a single word # noqa: E501

    :param word_id: ID of word to return
    :type word_id: str

    :rtype: Word

    return 'do some magic!'
    """
    if word_id in config.words.keys():
        return config.words_ref.document(word_id).get().to_dict()
    else:
        return None


def update_word(body=None):  # noqa: E501
    """Update an existing word

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Word.from_dict(connexion.request.get_json())  # noqa: E501
    
    # Document reference in the database
    doc_ref = config.words_ref.document(body.id)
    
    # Update the document
    for attribute in body.attribute_map:
        doc_ref.update({attribute: getattr(body, attribute)})

    return True


def update_word_with_form(word_id, name=None, status=None):  # noqa: E501
    """Updates a word in the store with form data

     # noqa: E501

    :param word_id: ID of word that needs to be updated
    :type word_id: str
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
    :type word_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        body = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
