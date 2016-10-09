from flask import Flask, redirect, render_template, request, session, url_for, redirect, jsonify
import json
from flask.ext.pymongo import PyMongo

muchsentiment = Flask(__name__)

muchsentiment.config['MONGO_DBNAME'] = 'prod'
muchsentiment.config['MONGO_URI'] = 'mongodb://ec2-52-38-154-245.us-west-2.compute.amazonaws.com:27017/prod'

mongo = PyMongo(muchsentiment)

# Just do all of the routing in here
@muchsentiment.route('/')
def main():
  return redirect('/index')

@muchsentiment.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  muchsentiment.run(debug=True)
