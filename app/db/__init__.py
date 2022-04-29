import logging
import os

from flask import Blueprint, cli
from flask_sqlalchemy import SQLAlchemy

from app import config

db = SQLAlchemy()

database = Blueprint('database', __name__,)

@database.cli.command('create')
def init_db():
    db.create_all()


