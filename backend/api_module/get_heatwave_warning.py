from urllib.parse import urlencode, unquote, quote_plus
import os
import json
import requests
import openpyxl
from bs4 import BeautifulSoup
from datetime import datetime
from collections import OrderedDict

FILE_PATH = "./api_json/test_warning_data.json"
EXCEL_PATH = "./area_code.xlsx"

serviceKey = "IQKSvGnIHGhpehEOPDmuuIWdUZ6NEZBoShPV0eLw8rLGqxxq3RAZWa7UV8EDQKSHQybcqwuJaJjufR5NZXDjeg=="
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')


def read_area_excel_file(file: EXCEL_PATH):
    filename = EXCEL_PATH  # 파일명
    book = openpyxl.load_workbook(filename)  # 엑셀 파일 book 변수에 저장
    sheet = book.worksheets[0]  # 첫번쨰 워크 시트 저장

    data = dict()
    for row in sheet.rows:  # 전체 행에 대하여 반복 실행
        data[row[2].value] = row[0].value

    return data


def get_heatwave_warning_data():
    """
        폭염 위험 수준 조회 : http://apis.data.go.kr/1360000/ImpactInfoService/getHWImpactValue
        한파 위험 수준 조회 : http://apis.data.go.kr/1360000/ImpactInfoService/getCWImpactValue
        폭염 영향 분야 (1.보건(일반인), 2.보건(취약인), 3.산업, 4.축산업, 5.농업, 6.수산양식, 7.기타)
    """

    now = datetime.now()
    current_time = f"{now.year}{now.month}{now.day}"

    url = "http://apis.data.go.kr/1360000/ImpactInfoService/getHWImpactValue"
    pageNo = "1"
    numOfRows = "40"
    dataType = "json"
    regId_dict = read_area_excel_file(EXCEL_PATH)
    tm = current_time

    data = OrderedDict()

    for regId in regId_dict.keys():
        query_params = '?' + urlencode({quote_plus('ServiceKey'): serviceKeyDecoded, quote_plus('dataType'): dataType,
                                        quote_plus('numOfRows'): numOfRows, quote_plus('pageNo'): pageNo,
                                        quote_plus('regId'): regId_dict[regId], quote_plus('tm'): tm
                                        })
        res = requests.get(url + query_params)
        soup = BeautifulSoup(res.content, 'html.parser')
        day_json = json.loads(soup.text)
        data[regId] = day_json

    write_json_file(FILE_PATH, data)


def warning_data_parsing():
    if not os.path.isfile(FILE_PATH):
        get_heatwave_warning_data()

    with open(FILE_PATH, "r") as json_file:
        warning_dict = json.load(json_file)

    return_dict = dict()

    for region in warning_dict.keys():
        if warning_dict[region]['response']['header']['resultMsg'] == "NO_DATA":
            continue

        items = warning_dict[region]['response']['body']['items']['item']
        warning_list = items

        return_dict[items[0]['regId']] = warning_list

    return_data = json.dumps(return_dict, ensure_ascii=False, indent='\t')

    return return_data


def write_json_file(path, data):
    with open(path, 'w') as total_outfile:
        json.dump(data, total_outfile, ensure_ascii=False)
