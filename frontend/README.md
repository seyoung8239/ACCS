# ACCS: Web Frontend 

## 사용기술 
 - React 
 - deck.gl 
 - chart.js 
 - Firestore 
 - firebase hosting 

## 실행방법 
- 배포된 서비스 이용 (아래 url로 접근 가능)
> codingpotato-6daf2.web.app
- Local환경에서 실행 (React)
```
cd frontend
npm start
```

## 기능 설명
### 전국 무더위쉼터 지도 
- 지도에 무더위 쉼터의 위치를 표현
  (tooltip을 통해 근처 쉼터 갯수, 좌표 정보 제공)
- 각 지역의 하루 최대기온, 평균기온, 최소기온, 위험도를 표현
### 온열질환자 데이터
- 각 년도 기준 전체환자, 실외환자, 실내환자 수를 제공
- 각 년도 지역별 환자의 분포를 차트를 통해 표현
### 지원요청 게시판 
- 폭염 위험에 대처하기 위한 지원요청 게시판
- Firestore와 연동해 CRUD 구현 
