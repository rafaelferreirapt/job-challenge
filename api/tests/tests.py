import unittest
import json
import os
import sys
import xmlrunner
import logging

sys.path.insert(1, os.path.join(sys.path[0], '..'))


from api import app


class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_types(self):
        # email
        response = self.app.post("/api/v1/email/", data=json.dumps({
            "email": "1380@robinhood.sch.bham.co.uk"
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        resp_json = json.loads(response.data)
        self.assertEqual(resp_json, {u'result': [u'neopets']})

        # domains

        response = self.app.post("/api/v1/domain/", data=json.dumps({
            "domain": "robinhood.sch.bham.co.uk"
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        resp_json = json.loads(response.data)
        self.assertEqual(resp_json, {u'result': [u'neopets']})


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
