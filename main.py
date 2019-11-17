from random import choice

from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

# Enable CORS (cross-origin resource sharing) if frontend and backend runs on the same server (e.g. local dev host).
# from flask_cors import CORS

from pprint import pprint

app = Flask(__name__)
# CORS(app)
api = Api(app)

# Should move to a database
words = [{'id': 1, 'name': 'cow', 'imageurl': 'cow.jpg'},
         {'id': 2, 'name': 'dog', 'imageurl': 'dog.jpg'},
         {'id': 3, 'name': 'mouse', 'imageurl': 'mouse.jpg'},
         {'id': 4, 'name': 'train', 'imageurl': 'train.jpeg'},
         {'id': 5, 'name': 'goose', 'imageurl': '318px-Domestic_Goose_(2).jpg'},
         {'id': 6, 'name': 'horse', 'imageurl': '320px-Horse_2005-08-06_(Cheval).jpg'},
         {'id': 7, 'name': 'juice', 'imageurl': 'juice-306748_960_720.png'},
         {'id': 8, 'name': 'pig', 'imageurl': 'pig.jpg'},
         {'id': 9, 'name': 'rooster', 'imageurl': 'rooster.jpg'},
         {'id': 10, 'name': 'mama', 'imageurl': 'mama.jpg'},
         {'id': 11, 'name': 'papa', 'imageurl': 'papa.jpg'},
         {'id': 12, 'name': 'sasha', 'imageurl': 'sasha.jpg'},
         {'id': 13, 'name': 'dima', 'imageurl': 'dima.jpg'},
         {'id': 14, 'name': 'cat', 'imageurl': '320px-Felis_catus-cat_on_snow.jpg'}
         ]

# Stores learned words
words_learned = list()


# Parses HTML request. TODO(romanklyuev): replace with modern alternative (check the docs)
word_parser = reqparse.RequestParser()
word_parser.add_argument('id', type=int)
word_parser.add_argument('name', type=str)
word_parser.add_argument('imageurl', type=str)


class Words(Resource):

    def get(self):
        global words_learned

        if len(words) - len(words_learned) < 3:
            print(len(words))
            print(len(words_learned))
            words_learned = list()

        words_not_learned = [word for word in words if word['name'] not in words_learned]

        words_to_learn = list()
        while len(words_to_learn) < 3:
            candidate = choice(words_not_learned)
            if candidate not in words_to_learn:
                words_to_learn.append(candidate)

        return jsonify(words_to_learn)

    def post(self):
        """Adds new word."""
        new_word = word_parser.parse_args()
        # Generate ID for the word
        new_word['id'] = len(words) + 1
        words.append(new_word)
        pprint(words)
        return new_word

    def put(self):
        """Updates the word."""
        word_to_update = word_parser.parse_args()
        for word in words:
            if word['id'] == word_to_update['id']:
                word_index = words.index(word)
                words.remove(word)
                words.insert(word_index, word_to_update)
        pprint(words)
        return word_to_update


"""
# FINISH LATER
class WordsToLearn(Resource):
    def get(self, number_of_words):
        if 0 < number_of_words < 10:
            return jsonify(words[0:number_of_words])
        else:
            return 'Error'
"""


class WordId(Resource):

    def get(self, word_id):
        for word in words:
            if word['id'] == word_id:
                return jsonify(word)
        else:
            return 'Error'


class SearchWords(Resource):

    def get(self, term):
        """Returns all words, which have the term in their name."""

        output = list()
        for word in words:
            if term in word['name']:
                output.append(word)
        return jsonify(output)


class WordLearned(Resource):
    """Manages words, which current user know (learned)."""

    def get(self):
        """Returns learned words."""
        return words_learned

    def put(self):
        """Adds new word, that have been just learned, to the learned words."""
        args = word_parser.parse_args()
        words_learned.append(args['name'])
        return args


api.add_resource(Words, '/words')
# api.add_resource(WordsToLearn, '/words/<int:number_of_words>')
api.add_resource(WordId, '/words/<int:word_id>')
api.add_resource(SearchWords, '/words/search/<string:term>')
api.add_resource(WordLearned, '/learned')

if __name__ == '__main__':
    app.run(debug=True)
