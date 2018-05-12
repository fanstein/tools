# coding:utf8
import json
from Common import Common


class GetFromJson(Common):
    def __init__(self, json_data):
        super(GetFromJson, self).__init__()
        self.json_data = json_data

    @Common.log("is_json")
    def is_json(self):
        try:
            # json_str = json.dumps(self.json_data)
            json.loads(self.json_data)
        except ValueError:
            return False
        return True

    def data(self):
        if self.is_json():
            pass
        pass
    print json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])


if __name__ == '__main__':
    json_data = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
    print GetFromJson(json_data).is_json()
