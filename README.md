# ACCS: Web Backend
## 사용기술
  - Django
  - WebSocket
  - BeautifulSoup
  - channels
  - docker
  - redis
- 배포된 서비스 이용(아래 url로 접근 가능)
> http://34.64.174.66:8000/
 ```
 cd backend
 python manage.py runserver
 ```
 ### 기능 설명
 /heatwave/total
 > 온열질환자에 대한 전국 통계 api
 
 /heatwave/region
 > 온열질환자에 대한 지역별 통계 api
 
 /heatwave/response/<field>
 > 온열 대처요령 category별 api
 
 /shelter
 > 전국 무더위쉼터 정보 및 위치
 
 /ShareMe
 > 사용자 위치별 가장 가까운 무더위쉼터 정보, category별 대처요령 유저에게 socket을 통해 전송
 
 /Alarm
 > socket을 통해 전달받은 정보 표시
 
