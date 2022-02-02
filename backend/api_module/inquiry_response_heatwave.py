from urllib.parse import urlencode, unquote, quote_plus
import os
import json
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

FILE_PATH = "./api_json/all_categories_heatwave_response.json"
# (1.보건(일반인), 2.보건(취약인), 3.산업, 4.축산업, 5.농업, 6.수산 양식, 7.기타)
ALL_CATEGORIES = ['public', 'vulnerable', 'industry', 'livestock', 'agriculture', 'aquaculture', 'etc']

serviceKey = "IQKSvGnIHGhpehEOPDmuuIWdUZ6NEZBoShPV0eLw8rLGqxxq3RAZWa7UV8EDQKSHQybcqwuJaJjufR5NZXDjeg=="
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')


def get_action_by_field(field):
    """ 폭염시 분야별 행동 요령 데이터 """

    if not os.path.isfile(FILE_PATH):  # json 파일이 존재 X
        load_all_response_standards_heatwave()

    with open(FILE_PATH, "r") as json_file:
        data = json.load(json_file)

    return data[field]


def load_all_response_standards_heatwave():
    """
       한파분야별대응기준조회 : http://apis.data.go.kr/1360000/ImpactInfoService/getCWCntrmsrMthd
       폭염 영향 분야 (1.보건(일반인), 2.보건(취약인), 3.산업, 4.축산업, 5.농업, 6.수산 양식, 7.기타)
    """

    url = "http://apis.data.go.kr/1360000/ImpactInfoService/getHWCntrmsrMthd"
    pageNo = "1"
    numOfRows = "100"
    dataType = "JSON"

    data = OrderedDict()

    for clsfc, category in enumerate(ALL_CATEGORIES):
        query_params = '?' + urlencode({quote_plus('ServiceKey'): serviceKeyDecoded, quote_plus('dataType'): dataType,
                                        quote_plus('numOfRows'): numOfRows, quote_plus('pageNo'): pageNo,
                                        quote_plus('clsfc'): str(clsfc + 1)
                                        })
        res = requests.get(url + query_params)
        soup = BeautifulSoup(res.content, 'html.parser')

        to_dict = json.loads(soup.text)  # json 형태로 받아온 api 데이터 python dict 형태로 변경
        if to_dict['response']['header']['resultCode'] == '00':
            response_list = to_dict['response']['body']['items']['item']
            data[category] = response_list

    write_json_file(data)


def write_json_file(data):
    """ 분야별 폭염 대처 방안 데이터 json 파일에 저장 """

    with open(FILE_PATH, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent='\t')