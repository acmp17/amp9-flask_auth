import logging
from logging.config import dictConfig

import flask
from flask import request, current_app

from app.logging_config.log_formatters import RequestFormatter

log_con = flask.Blueprint('log_con', __name__)


@log_con.before_app_request
def before_request_logging():
    current_app.logger.info("Before Request")
    log = logger.getLogger("myApp")
    log.info ("My App Logger")


@log_con.after_app_request
def after_request_logging(response):
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response
    elif request.path.startswith('/bootstrap'):
        return response
    current_app.logger.info("After Request")

    log = logger.getLogger("myApp")
    log.info("My App Logger")
    return response


@log_con.before_app_first_request
def configure_logging()
    logging.config.dictConfig(LOGGING_CONFIG)
    log = logging.getLogger("myApp")
    log.info("My App Logger")
    log = logging.getLogger("myerrors")
    log.info("This broke")




LOGGING_CONFIG = {
    'version': 1,

}
