# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import, division, print_function
from flask import Flask
from flask.ext.twip import Twip
from flask.ext.twip.backend import FileBackend
from flask.ext.twip.environment import WSGIEnvironment

app = Flask(__name__)
app.config.from_object('settings')
be = FileBackend(folder='tokens')
twip = Twip(app, backend=be, environment=WSGIEnvironment)
