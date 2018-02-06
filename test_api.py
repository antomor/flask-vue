import unittest
import json
import os
from app import app

class ApiTestCase(unittest.TestCase):

    def setUp(self):
        app.config['Mode'] = 'Testing'
        self.app = app
        self.client = self.app.test_client

    def tearDown(self):
        pass

    def test_get_all_risk_types(self):
        res = self.client().get('/api/risk-types/')
        self.assertEqual(res.status_code, 200)
    
    def test_get_risk_types_by_id(self):
        res = self.client().get('/api/risk-types/1')
        self.assertEqual(res.status_code, 200)

def main():
    unittest.main()

if __name__ == '__main__':
    main()