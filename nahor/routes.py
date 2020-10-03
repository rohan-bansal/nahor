from flask import Flask, request, render_template, redirect, Blueprint
from . import db
from .models import Shortify
import base64, hashlib
from urllib.parse import urlparse
import random

routes = Blueprint('routes', __name__)

host = 'http://nahor.cf/'

shady_words_1 = ['goat', 'virus', 'malware', 'downloadram', 'paypal', 'password', 'keylog', 'killstick', 'tax', 'windows10']
shady_words_2 = ['exe', 'msi', 'zip', 'tar', 'virzip', 'tar.gz', 'trojan', 'worm']
random_symbols = ['~', '!', '=', '@']


def hashify(value, digits=5):
    return(hashlib.md5(value.encode('utf-8')).hexdigest())[:digits]

def shadify(value):
    baseShady = ""
    baseShady += random.choice(shady_words_1) + str(random.randint(1, 100)) + "-" + random.choice(shady_words_1) + random.choice(random_symbols) + random.choice(random_symbols)
    baseShady += "." + random.choice(shady_words_2) + "." + random.choice(shady_words_2)
    return baseShady

@routes.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form.get('url')
        method = request.form['radio_option']

        if '.' not in original_url:
            return render_template('index.html')

        if urlparse(original_url).scheme == '':
            url = 'http://' + original_url
        else:
            url = original_url

        if method == "hashed":
            url_identifier = hashify(url)
        else:
            url_identifier = shadify(url)

        if Shortify.query.filter_by(hash_identifier=url_identifier).first() == None:
            db.session.add(Shortify(hash_identifier=url_identifier, original_url = url))
            db.session.commit()

        return render_template('index.html', short_url = host + url_identifier)
        
    return render_template('index.html')


@routes.route('/<short_url>')
def redirect_short_url(short_url):
    url = host

    var = Shortify.query.filter_by(hash_identifier=short_url).first()
    if var is not None:
        url = var.original_url
    
    return redirect(url)