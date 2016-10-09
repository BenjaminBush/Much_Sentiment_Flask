from flask import Flask, render_template, request, redirect
import flask.ext.pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'prod'
app.config['MONGO_URI'] = 'mongodb://ec2-52-38-154-245.us-west-2.compute.amazonaws.com:27017/prod'

mongo = PyMongo(app)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('api/speakers')
def getSpeakers():
	speakers = mongo.db.speakers
	result = speakers.find({})
	return result

if __name__ == '__main__':
  app.run(port=33507)
