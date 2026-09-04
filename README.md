# Crowd Sentiment Analyzer

네이버 검색 관심도 데이터를 수집하고 OpenAI API를 이용해 검색 관심도의 흐름을 분석하는 Python CLI 프로젝트입니다.

사용자가 검색어와 분석 기간을 입력하면 네이버 DataLab API에서 검색 관심도 데이터를 가져온 뒤, OpenAI API를 통해 추세와 관심 집중 시점을 분석합니다.

## 주요 기능

* 사용자 검색어 입력
* 분석 기간 선택

  * 1주일
  * 2주일
  * 1개월
  * 2개월
  * 6개월
* Naver DataLab API를 통한 검색 관심도 데이터 수집
* OpenAI API를 통한 검색 관심도 분석
* 분석 결과를 JSON 형식으로 출력

## 분석 항목

OpenAI API는 다음 항목을 분석합니다.

* `trend`
  검색 관심도의 상승·하락 흐름

* `concentration`
  검색 관심도가 집중된 시점이나 패턴

* `attention_spike`
  평소 흐름 대비 급격한 관심 증가 여부

> Naver DataLab의 `ratio` 값은 절대 검색량이나 퍼센트가 아니라, 분석 기간 내 검색 관심도를 정규화한 상대 지수입니다.

따라서 이 프로젝트는 검색 관심도만으로 주가 방향, 긍정·부정 감정, 매수·매도 의도 등을 판단하지 않습니다.

## 프로젝트 구조

```text
crowd-sentiment-analyzer/
├── main.py
├── naver_api.py
├── openai_api.py
├── .env.example
├── .gitignore
└── README.md
```

### main.py

프로그램의 전체 흐름을 관리합니다.

```text
사용자 입력
    ↓
기간 데이터 생성
    ↓
Naver API 호출
    ↓
OpenAI API 분석
    ↓
결과 출력
```

### naver_api.py

Naver DataLab API 요청을 담당합니다.

### openai_api.py

Naver API에서 받은 검색 관심도 데이터를 OpenAI API에 전달하고 구조화된 분석 결과를 반환합니다.

## 환경변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 다음 값을 입력합니다.

```text
Client_ID=YOUR_NAVER_CLIENT_ID
Client_Secret=YOUR_NAVER_CLIENT_SECRET
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

실제 API Key가 포함된 `.env` 파일은 Git에 업로드하지 않습니다.

`.env.example`에는 필요한 환경변수 이름만 포함되어 있습니다.

## 설치

필요한 Python 패키지를 설치합니다.

```bash
pip install requests python-dotenv openai pydantic
```

## 실행

```bash
python main.py
```

실행 후 메뉴에서 검색을 선택하고 검색어와 분석 기간을 입력합니다.

예시:

```text
1. 데이터 검색
2. 프로그램 종료

숫자를 입력해주세요> 1

검색어 입력> 삼전 주가

[기간 선택]
1. 1주일
2. 2주일
3. 1개월
4. 2개월
5. 6개월
```

분석이 완료되면 다음과 같은 형태로 결과가 출력됩니다.

```json
{
    "startDate": "2026-08-05",
    "endDate": "2026-09-04",
    "trend": "검색 관심도의 전체적인 흐름",
    "concentration": "관심도가 집중된 시점",
    "attention_spike": "주변 흐름 대비 관심 급증 여부"
}
```

## 사용 기술

* Python
* Naver DataLab API
* OpenAI API
* Requests
* python-dotenv
* Pydantic
* Git / GitHub

## 프로젝트 목적

Python을 이용한 API 활용과 여러 Python 파일 간 데이터 전달 구조를 복습하기 위해 제작했습니다.

특히 다음 내용을 직접 구현하는 것을 목표로 했습니다.

* REST API 요청 및 응답 처리
* JSON 데이터 처리
* 외부 API 2개 연결
* Python 모듈 분리
* 환경변수를 이용한 API Key 관리
* Pydantic을 이용한 구조화된 AI 응답
* Git / GitHub를 이용한 버전 관리