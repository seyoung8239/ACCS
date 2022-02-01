from urllib.parse import urlencode, unquote, quote_plus
import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from collections import OrderedDict

TOTAL_FILE_PATH = "./api_json/total_heat_wave.json"
REGION_FILE_PATH = "./api_json/region_heat_wave.json"

TOTAL_DATA = OrderedDict()  # 연도별 사상자 수
REGION_DATA = OrderedDict()  # 연도별, 지역별 사상자 수

serviceKey = "IQKSvGnIHGhpehEOPDmuuIWdUZ6NEZBoShPV0eLw8rLGqxxq3RAZWa7UV8EDQKSHQybcqwuJaJjufR5NZXDjeg=="
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')


def heatwave_casualties_total():
    """ 온열 환자 수 total 자료 """

    if not os.path.isfile(TOTAL_FILE_PATH):  # json 파일이 존재 X
        get_heatwave_data()

    with open(TOTAL_FILE_PATH, "r") as json_file:
        data = json.load(json_file)

    return data


def heatwave_casualties_region():
    """ 온열 환자 수 region 별 자료 """

    if not os.path.isfile(REGION_FILE_PATH):  # json 파일이 존재 X
        get_heatwave_data()

    with open(REGION_FILE_PATH, "r") as json_file:
        data = json.load(json_file)

    return data


def get_heatwave_data():
    """ open api 로부터 온열 환자 데이터 (json 형태로) 받아 오는 함수 """

    url = "http://apis.data.go.kr/1741000/HeatWaveCasualtiesRegion/getHeatWaveCasualtiesRegionList"
    returnType = "xml"
    numOfRows = "18"
    pageNo = "1"

    now = datetime.now()
    current_year = int(now.year)

    for year in range(2016, current_year):
        query_params = '?' + urlencode({quote_plus('ServiceKey'): serviceKeyDecoded, quote_plus('type'): returnType,
                                        quote_plus('numOfRows'): numOfRows, quote_plus('pageNo'): pageNo,
                                        quote_plus('bas_yy'): year
                                        })
        res = requests.get(url + query_params)
        soup = BeautifulSoup(res.text, 'lxml-xml')
        xml_data = soup.find_all('row')

        if len(xml_data) > 0:
            total_data = xml_data[0]
            region_data = xml_data[1:]

            TOTAL_DATA[str(year)] = xml_to_dict(total_data)
            REGION_DATA[str(year)] = list()

            for rd in region_data:
                REGION_DATA[str(year)].append(xml_to_dict(rd))

        total_json = json.dumps(TOTAL_DATA, ensure_ascii=False, indent='\t')  # total dict to json
        region_json = json.dumps(REGION_DATA, ensure_ascii=False, indent='\t')  # region dict to json

        write_json_file(total_json, region_json)  # 받아온 total, region 온열 질환자 데이터 json 파일로 저장


def xml_to_dict(obj):
    """ xml 형태의 bs4 객체를 dict 형태로 변환 """

    to_json = dict()

    to_json["year"] = obj.find('bas_yy').get_text()
    to_json['region'] = obj.find('regi').get_text()
    to_json['total'] = obj.find('tot').get_text()
    to_json['otdoor_subtot'] = obj.find('otdoor_subtot').get_text()
    to_json['otdoor_otdoor_wrkpl'] = obj.find('otdoor_otdoor_wrkpl').get_text()
    to_json['otdoor_field'] = obj.find('otdoor_field').get_text()
    to_json['otdoor_farmland'] = obj.find('otdoor_farmland').get_text()
    to_json['otdoor_mountain'] = obj.find('otdoor_mountain').get_text()
    to_json['otdoor_river'] = obj.find('otdoor_river').get_text()
    to_json['otdoor_road'] = obj.find('otdoor_road').get_text()
    to_json['otdoor_etc'] = obj.find('otdoor_etc').get_text()
    to_json['indoor_subtot'] = obj.find('indoor_subtot').get_text()
    to_json['indoor_house'] = obj.find('indoor_house').get_text()
    to_json['indoor_bildg'] = obj.find('indoor_bildg').get_text()
    to_json['indoor_wrkpl'] = obj.find('indoor_wrkpl').get_text()
    to_json['indoor_greenhouse'] = obj.find('indoor_greenhouse').get_text()
    to_json['indoor_etc'] = obj.find('indoor_etc').get_text()

    return to_json


def write_json_file(total, region):
    """ total, region 온열 질환자 데이터 json 파일에 저장 """

    with open(TOTAL_FILE_PATH, 'w') as total_outfile:  # total
        json.dump(total, total_outfile, ensure_ascii=False, indent='\t')
    with open(REGION_FILE_PATH, 'w') as region_outfile:  # regions
        json.dump(region, region_outfile, ensure_ascii=False, indent='\t')
