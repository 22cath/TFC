import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
# app.config.from_object("config")

import my_crypto.db
import my_crypto.api
import models
