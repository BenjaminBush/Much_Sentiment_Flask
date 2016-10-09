from flask import Flask, render_template, request, redirect
from flask.ext.pymongo import PyMongo

muchsentiment = Flask(__name__)

muchsentiment.config['MONGO_DBNAME'] = 'prod'
muchsentiment.config['MONGO_URI'] = 'mongodb://ec2-52-38-154-245.us-west-2.compute.amazonaws.com:27017/prod'
muchsentiment.config['MONGO_USERNAME'] = 'dembois'
muchsentiment.config['MONGO_PASSWORD'] = 'coldlikeminnesota'

mongo = PyMongo(muchsentiment)


from routes.views import *

@muchsentiment.route('/')
def main():
  return redirect('/index')

@muchsentiment.route('/index')
def index():
  return render_template('index.html')

@muchsentiment.route('api/speakers', methods=['GET'])
def getSpeakers():
	speakers = mongo.db.speakers
	result = speakers.find({})
	return result

if __name__ == '__main__':
  muchsentiment.run(port=33507)
