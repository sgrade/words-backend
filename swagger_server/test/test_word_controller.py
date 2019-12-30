# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.word import Word  # noqa: E501
from swagger_server.test import BaseTestCase


class TestWordController(BaseTestCase):
    """WordController integration test stubs"""

    def test_add_word(self):
        """Test case for add_word

        Add a new word to the store
        """
        body = Word()
        response = self.client.open(
            '/sgrade/words/1.0.0/word',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_word(self):
        """Test case for delete_word

        Deletes a word
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/sgrade/words/1.0.0/word/{wordId}'.format(word_id=789),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_word_by_id(self):
        """Test case for get_word_by_id

        Find word by ID
        """
        response = self.client.open(
            '/sgrade/words/1.0.0/word/{wordId}'.format(word_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_word(self):
        """Test case for update_word

        Update an existing word
        """
        body = Word()
        response = self.client.open(
            '/sgrade/words/1.0.0/word',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_word_with_form(self):
        """Test case for update_word_with_form

        Updates a word in the store with form data
        """
        data = dict(name='name_example',
                    status='status_example')
        response = self.client.open(
            '/sgrade/words/1.0.0/word/{wordId}'.format(word_id=789),
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upload_file(self):
        """Test case for upload_file

        uploads an image
        """
        body = Object()
        response = self.client.open(
            '/sgrade/words/1.0.0/word/{wordId}/uploadImage'.format(word_id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/octet-stream')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
