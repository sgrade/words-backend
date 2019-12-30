# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.words import Words  # noqa: E501
from swagger_server.test import BaseTestCase


class TestWordsController(BaseTestCase):
    """WordsController integration test stubs"""

    def test_find_words_by_name(self):
        """Test case for find_words_by_name

        Find Words by name
        """
        response = self.client.open(
            '/sgrade/words/1.0.0/words/findByName'.format(term='term_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_words_by_status(self):
        """Test case for find_words_by_status

        Finds Words by status
        """
        query_string = [('status', 'notStarted')]
        response = self.client.open(
            '/sgrade/words/1.0.0/words/findByStatus',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_words_to_learn(self):
        """Test case for get_words_to_learn

        Get words to learn
        """
        query_string = [('limit', 4),
                        ('status', 'status_example')]
        response = self.client.open(
            '/sgrade/words/1.0.0/words',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
