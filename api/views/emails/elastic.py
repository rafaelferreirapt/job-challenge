#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
from settings import TYPES, ELASTIC_HOST, ELASTIC_PORT


def strict_email(email):
    result = []

    for leak in TYPES:
        r = requests.get(url="http://"+ELASTIC_HOST+":"+ELASTIC_PORT+"/binary/"+leak+"/_count?q=email:"+email)

        json_result = json.loads(r.text)

        if "count" in json_result and json_result["count"] > 0:
            result += [leak]

    return {"result": result}


def search_domain(domain_name):
    result = []

    for leak in TYPES:
        r = requests.get(url="http://"+ELASTIC_HOST+":"+ELASTIC_PORT+"/binary/"+leak+"/_count",
                         headers={'Content-Type': 'application/json'},
                         json={
                             "query": {
                                 "wildcard": {
                                     "email": {
                                         "value": "*@"+domain_name
                                     }
                                 }
                             }
                         })

        json_result = json.loads(r.text)

        if "count" in json_result and json_result["count"] > 0:
            result += [leak]

    return {"result": result}


if __name__ == '__main__':
    # only for testing
    print "domain: " + str(search_domain("qq.com"))
    print "strict_email: " + str(strict_email("1380@robinhood.sch.bham.co.uk"))
