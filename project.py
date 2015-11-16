from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

import httplib2
import json

import requests
import pdb

app = Flask(__name__)

APPLICATION_NAME = "Hurizen"

@app.route('/')
def homePage(): 
	return 'hello world'


if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
