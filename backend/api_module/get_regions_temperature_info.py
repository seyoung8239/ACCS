from urllib.parse import urlencode, unquote, quote_plus
import os
import json
import requests
from bs4 import BeautifulSoup

FILE_PATH = "./api_json/test_weather.json"

serviceKey = "IQKSvGnIHGhpehEOPDmuuIWdUZ6NEZBoShPV0eLw8rLGqxxq3RAZWa7UV8EDQKSHQybcqwuJaJjufR5NZXDjeg=="
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')


def get_weather_day():
    url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList"
    pageNo = "1"
    numOfRows = "50"
    dataType = "json"
    dataCd = "ASOS"
    dateCd = 'DAY'
    startDt = '20210729'
    endDt = '20210729'
    areas = """
        {"백령도" : "102",
        "서울" : "108",
        "강릉" : "105",
        "인천" : "112",
        "울릉도" : "115",
        "수원" : "119",
        "충청북도 청주" : "131",
        "충청남도 홍성" : "177",
        "대전" : "133",
        "경상북도 안동" : "136",
        "경상북도 포항시" : "138",
        "대구" : "143",
        "울산광역시 중구" : "152",
        "경상남도 창원시" : "155",
        "부산" : "159",
        "전라북도 전주" : "146",
        "광주광역시 북구" : "156",
        "전라남도 목포" : "165",
        "전라남도 여수" : "168",
        "제주" : "184"}
    """

    weather_area = json.loads(areas)
    weather_info = list()

    for area in weather_area.keys():
        queryParams = '?' + urlencode({quote_plus('ServiceKey'): serviceKeyDecoded, quote_plus('dataType'): dataType,
                                       quote_plus('numOfRows'): numOfRows, quote_plus('pageNo'): pageNo,
                                       quote_plus('dataCd'): dataCd, quote_plus('dateCd'): dateCd,
                                       quote_plus('startDt'): startDt, quote_plus('endDt'): endDt,
                                       quote_plus('stnIds'): weather_area[area]
                                       })
        res = requests.get(url + queryParams)
        soup = BeautifulSoup(res.content, 'html.parser')
        info_json = json.loads(soup.text)
        weather_info.append({area: info_json})

    write_json_file(FILE_PATH, weather_info)


def weather_info_parsing():
    if not os.path.isfile(FILE_PATH):
        get_weather_day()

    with open(FILE_PATH, "r") as json_file:
        info_list = json.load(json_file)

    parsed_data = list()

    for info in info_list:
        parsing_dict = dict()
        info = list(info.values())
        parsing_data = info[0]['response']['body']['items']['item'][0]

        parsing_dict["stnId"] = parsing_data["stnId"]
        parsing_dict["stnNm"] = parsing_data["stnNm"]
        parsing_dict["time"] = parsing_data["tm"]
        parsing_dict["avgTa"] = parsing_data["avgTa"]
        parsing_dict["maxTa"] = parsing_data["maxTa"]
        parsing_dict["minTa"] = parsing_data["minTa"]

        if float(parsing_dict['maxTa']) >= 35:
            parsing_dict['value'] = "심각"
        elif float(parsing_dict['maxTa']) >= 33:
            parsing_dict['value'] = "경고"
        elif float(parsing_dict['maxTa']) >= 30:
            parsing_dict['value'] = "주의"
        elif float(parsing_dict['maxTa']) >= 27:
            parsing_dict['value'] = "관심"
        else:
            parsing_dict['value'] = "평화"

        parsed_data.append(parsing_dict)

    return_data = json.dumps(parsed_data, ensure_ascii=False, indent='\t')

    return return_data


def write_json_file(path, data):
    with open(path, 'w') as total_outfile:
        json.dump(data, total_outfile, ensure_ascii=False)
