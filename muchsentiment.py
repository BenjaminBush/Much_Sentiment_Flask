from flask import Flask, redirect, render_template, request, session, url_for, redirect, jsonify
import json
from flask.ext.pymongo import PyMongo

muchsentiment = Flask(__name__)

muchsentiment.config['MONGO_DBNAME'] = 'prod'
muchsentiment.config['MONGO_URI'] = 'mongodb://ec2-52-38-154-245.us-west-2.compute.amazonaws.com:27017/prod'

mongo = PyMongo(muchsentiment)

class speaker(object):
    def __init__(self, election_result, name, state, incumbent, year, party, _id, speaker_id):
        self.election_result = election_result
        self.name = name
        self.state = state
        self.incumbent = incumbent
        self.year = year
        self.party = party
        self._id = _id
        self.speaker_id = speaker_id
    def serialize(self):
        return {
                'election_result' : self.election_result,
                'name' : self.name,
                'state': self.state,
                'incumbent' : self.incumbent,
                'year' : self.year,
                'party' : self.party,
                '_id' : self._id,
                'speaker_id' : self.speaker_id,
                }
# Just do all of the routing in here
@muchsentiment.route('/')
def main():
  return redirect('/index')

@muchsentiment.route('/index')
def index():
    return render_template('index.html')
@muchsentiment.route('/api/speakers', methods=['GET'])
def getSpeaker():
        output = []
	speakers = mongo.db.speakers
        for speaker in speakers.find():
            output.append(speaker)       
        ret_dict = {}
        for i, val in enumerate(output):
            ret_dict[i]= val
        print(ret_dict)
        return jsonify(ret_dict.serialize())


if __name__ == '__main__':
  muchsentiment.run(debug=True)
