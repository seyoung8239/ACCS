import requests
import sys
import json
from datetime import datetime

APP_Key = "5ef736858613f8822fe61a60c2ec9efb"
URL = 'https://dapi.kakao.com/v2/local/geo/coord2regioncode.json'


def json_request(url="", encoding="utf-8", success=None,
                 error=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)):
    headers = {'Authorization': 'KakaoAK ' + APP_Key}
    # print('%s : success for request [%s]' % (datetime.now(), url))
    response = requests.get(url, headers=headers)
    return response.text


def reverse_geocode(longitude, latitude):
    url = '%s?x=%s&y=%s' % (URL, longitude, latitude)
    json_req = json_request(url=url)
    # print(json_req)
    try:
        json_req = json_request(url=url)
        json_data = json.loads(json_req)
        json_doc = json_data.get('documents')[1]
        json_name = json_doc.get('address_name')
        json_code = json_doc.get('code')
    except:
        json_name = "NaN"
        json_code = "NaN"
    return json_name, json_code


def get_address(x, y):
    address = []
    json_name, json_code = reverse_geocode(x, y)
    address.append(json_name)
    return address


def get_code(x, y):
    code = []
    json_name, json_code = reverse_geocode(x, y)
    code.append(json_code)
    return code


def make_code(longitude, latitude):
    code = get_code(longitude, latitude)
    return code


def make_address(longitude, latitude):
    address = get_address(longitude, latitude)
    return address
