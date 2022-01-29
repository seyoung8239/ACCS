import json
import pprint
from urllib.parse import urlencode, unquote, quote_plus
import requests
from lxml import html
from bs4 import BeautifulSoup
from collections import OrderedDict

serviceKey = 'WC9CCzNYH/PEHu8JOYDKJfZ821AjbbnHk4mnWoSp8h1IUB/OgG+RKTiLo90IwPglMXN7WwhlmCugFCyh4F9YeA=='
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')
# # params = {'serviceKey':'P4%2BdEL2r5hyKVJj3z9Ce%2BaCLnWvxkWaFJNeTkLNDN6KTCf8xz5Nnub%2BW9%2BJVwFqjm%2FrrnrRcyPah3KHbgxQxQg%3D%3D', 'pageNo' : '1', 'numOfRows' : '3', 'type' : 'xml', 'year' : '2014', 'areaCd' : '1111051000', 'equptype' : '001' }
#
def check_place():
    url = 'http://apis.data.go.kr/1741000/HeatWaveShelter2/getHeatWaveShelterList2'
    params = {'serviceKey': serviceKey, 'type': 'xml', 'year': '2022',
               'equptype': '001'}
    response = requests.get(url, params = params)
    content = response.text
    # pp = pprint.PrettyPrinter(indent = 4)
    # print(pp.pprint(content))
    # subjects = {
    #     resSeqNo: 시설번호
    #     year: 년도
    #     areaCd: 지역코드
    #     equptype: 시설유형
    #     restname: 쉼터명
    #     restaddr: 소재지지번주소
    #     creDttm: 생성일시
    #     updtDttm: 수정일시
    #     useYn: 사용여부
    #     areaNm: 지역명
    #     operBeginDe: 운영시작일자
    #     operEndDe: 운영종료일자
    #     ar: 시설면적
    #     colrHoldElefn : 선풍기보유대수
    #     usePsblNmpr : 이용가능인원수
    #     colrHoldArcndtn : 에어컨보유대수
    #     chckMatterNightOpnAt: 야간개방
    #     chckMatterWkendHdayOpnAt: 휴일개방
    #     chckMatterStayngPsblAt: 숙박가능여부
    #     rm:특이사항
    #     dltAdres:소재지도로명주소
    #     mngdpt_cd:관리기관
    #     mngdptCd:관리기관 전화번호
    #     la:위도
    #     lo:경도
    # }
    soup = BeautifulSoup(content, "lxml-xml")
    rows = soup.find_all("row")
    shelter = ""
    for row in rows:
        file_data = OrderedDict()
        file_data["restSeqNo"] = row.find('restSeqNo').get_text()
        file_data["year"] = row.find('year').get_text()
        file_data["areaCd"] = row.find('areaCd').get_text()
        file_data["equptype"]= row.find('equptype').get_text()
        file_data["restname"]= row.find('restname').get_text()
        file_data["restaddr"]= row.find('restaddr').get_text()
        file_data["creDttm"]= row.find('creDttm').get_text()
        file_data["updtDttm"]= row.find('updtDttm').get_text()
        file_data["useYn"]= row.find('useYn').get_text()
        file_data["areaNm"]= row.find('areaNm').get_text()
        file_data["operBeginDe"]= row.find('operBeginDe').get_text()
        file_data["operEndDe"]= row.find('operEndDe').get_text()
        file_data["ar"] = row.find('ar').get_text()
        file_data["colrHoldElefn"] = row.find('colrHoldElefn').get_text()
        file_data["usePsblNmpr"] = row.find('usePsblNmpr').get_text()
        file_data["colrHoldArcndtn"] = row.find('colrHoldArcndtn').get_text()
        file_data["chckMatterNightOpnAt"]= row.find('chckMatterNightOpnAt').get_text()
        file_data["chckMatterWkendHdayOpnAt"]= row.find('chckMatterWkendHdayOpnAt').get_text()
        file_data["chckMatterStayngPsblAt"]= row.find('chckMatterStayngPsblAt').get_text()
        file_data["rm"]= row.find('rm').get_text()
        file_data["dtlAdres"]= row.find('dtlAdres').get_text()
        file_data["mngdpt_cd"]= row.find('mngdpt_cd').get_text()
        file_data["mngdptCd"]= row.find('mngdptCd').get_text()
        file_data["la"]= row.find('la').get_text()
        file_data["lo"]= row.find('lo').get_text()
        shelter += json.dumps(file_data, ensure_ascii=False, indent="\t")
    print(shelter)
    return content

