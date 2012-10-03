
from django.test import TestCase

import json



class FauneViewsTestCase(TestCase):
    def test_import(self):
        
        data = open('faune/data.json').read()
        jsonData = json.dumps(data)
        resp = self.client.post('/import/', {'data': data, 'token': '666'})

        self.assertEqual(resp.status_code, 200)
        
    #def test_export_sqlite(self):
    #    resp = self.client.post('/export/sqlite/', {'token': '666'})        
    #    self.assertEqual(resp.status_code, 200)
        
