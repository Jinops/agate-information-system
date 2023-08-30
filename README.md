# agate-infromation-system

Server of Agate Ltd.'s CMS
  
Agate 사의 광고 컨텐츠 관리 시스템(CMS) 서버

![class_diagram](/etc/class_diagram.png)


## 목적

1. Agate 회사의 CMS를 위한 서버를 개발합니다.
2. 가상의 요구사항에 맞는 광고 생성, 관리, 고객 연결 등의 기능을 개발합니다.
3. 각 기능을 Rest API로 제공합니다.

_기획 출처: Object-Oriented Systems Analysis and Design Using UML (2010, Simon Bennett & Ray Farmer)_

## 주요 기능
1. 고객 관리 (`/clinets`)
2. 캠페인(광고의 상위개념) 생성 및 관리, 스케쥴링 (`/campaigns`)
3. 광고 관리 (`/adverts`)
4. 직원 관리 (`/staffs`)
> 관리에는 CRUD를 포함하며, api_simple 문서에 추가적으로 명시되어 있습니다.

## 스펙
- Fast API 3.1버전을 통해 서버를 개발하였습니다.
- Replit을 통해 개발 및 테스트되었습니다.
- **DB가 없습니다.** 데이터는 entity 폴더 내 `db` 변수에 딕셔너리 형태로 저장됩니다.
- typing이 적용되어 있습니다.

## 부록 - frontend

![screenshot](/etc/frontend_screenshot.png)
