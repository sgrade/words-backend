from random import choice

from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

words = [{'id': 11, 'name': 'Cow', 'imageurl': 'cow.jpg'},
         {'id': 12, 'name': 'Dog', 'imageurl': 'dog.jpg'},
         {'id': 13, 'name': 'Mouse', 'imageurl': 'mouse.jpg'},
         {'id': 14, 'name': 'Train', 'imageurl': 'train.jpeg'},
         {'id': 16, 'name': 'Goose', 'imageurl': '318px-Domestic_Goose_(2).jpg'},
         {'id': 17, 'name': 'Horse', 'imageurl': '320px-Horse_2005-08-06_(Cheval).jpg'},
         {'id': 18, 'name': 'Juice', 'imageurl': 'juice-306748_960_720.png'},
         {'id': 19, 'name': 'Pig', 'imageurl': 'pig.jpg'},
         {'id': 20, 'name': 'Rooster', 'imageurl': 'rooster.jpg'},
         {'id': 22, 'name': 'Mama', 'imageurl': 'mama.jpg'},
         {'id': 23, 'name': 'Papa', 'imageurl': 'papa.jpg'},
         {'id': 24, 'name': 'Sasha', 'imageurl': 'sasha.jpg'},
         {'id': 25, 'name': 'Dima', 'imageurl': 'dima.jpg'}
         ]

words_learned = list()


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


class WordsToLearn(Resource):
    def get(self, number_of_words):
        if 0 < number_of_words < 10:
            return jsonify(words[0:number_of_words])
        else:
            return 'Error'


class Word(Resource):
    def get(self, word_id):
        for word in words:
            if word['id'] == word_id:
                return word
            else:
                return 'Error'

    def put(self, word_id):
        for word in words:
            if word['id'] == word_id:
                return 'The word already exists'
            else:
                words.append(request.form['data'])
                return word


word_parser = reqparse.RequestParser()
word_parser.add_argument('id', type=int)
word_parser.add_argument('name', type=str)
word_parser.add_argument('imageurl', type=str)


class WordLearned(Resource):
    def get(self):
        return words_learned

    def put(self):
        args = word_parser.parse_args()
        print(args)
        words_learned.append(args['name'])
        return args


api.add_resource(Words, '/words')
api.add_resource(WordsToLearn, '/words/<int:number_of_words>')
api.add_resource(Word, '/word/<int:word_id>')
api.add_resource(WordLearned, '/learned')

if __name__ == '__main__':
    app.run(debug=True)
