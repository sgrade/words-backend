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
         {'id': 15, 'name': 'Magneta', 'imageurl': 'mock-image.jpg'},
         {'id': 16, 'name': 'RubberMan', 'imageurl': 'mock-image.jpg'},
         {'id': 17, 'name': 'Dynama', 'imageurl': 'mock-image.jpg'},
         {'id': 18, 'name': 'Dr IQ', 'imageurl': 'mock-image.jpg'},
         {'id': 19, 'name': 'Magma', 'imageurl': 'mock-image.jpg'},
         {'id': 20, 'name': 'Tornado', 'imageurl': 'mock-image.jpg'}
         ]

words_learned = list()


class Words(Resource):
    def get(self):
        words_not_learned = [word for word in words if word['name'] not in words_learned]
        return jsonify(words_not_learned[0:3])


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
        """
        for word in words_learned:
            if word['id'] == word_id:
                return 'The word already exists'
            else:
                words_learned.append(request.form['data'])
                return word
        """


api.add_resource(Words, '/words')
api.add_resource(WordsToLearn, '/words/<int:number_of_words>')
api.add_resource(Word, '/word/<int:word_id>')
api.add_resource(WordLearned, '/learned')

if __name__ == '__main__':
    app.run(debug=True)
