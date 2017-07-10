# coding=utf-8
import logging
import sys
from flask import Blueprint, jsonify, request, abort
from elastic import strict_email, search_domain
from crossdomain import crossdomain
# flask routes

app = Blueprint('emails', __name__)
logging.basicConfig(stream=sys.stderr)
logging.getLogger().setLevel(logging.DEBUG)
log = logging.getLogger()


# end flask routes


@app.route("/email/", methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def api_email():
    content = request.json

    try:
        return jsonify(strict_email(content["email"]))
    except TypeError:
        abort(404)


@app.route("/domain/", methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def api_domain():
    content = request.json

    try:
        return jsonify(search_domain(content["domain"]))
    except TypeError:
        abort(404)
