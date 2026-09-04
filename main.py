from datetime import date, timedelta
from naver_api import naverSearch
from openai_api import Analysis
import json


def menu()->None:

    print('''
    1. 데이터 검색
    2. 프로그램 종료
    ''')

def UserSearch()->tuple[str,int]:

    User_str=input('검색어 입력>')

    while True:
        print()
        print('''
        [기간 선택]
        1. 1주일
        2. 2주일
        3. 1개월
        4. 2개월
        5. 6개월
        ''')
        try:
            User_int=input('숫자를 입력해주세요>')
            User_int=int(User_int)
        except ValueError:
            print('숫자를 입력해주세요')
            continue

        if 1<=User_int<=5:
            return (User_str, User_int)
        else:
            print()
            print('유효한 기간을 선택해주세요')
            continue

def dataFilter(data: tuple[str, int]) -> tuple[str, list[str]]:

    date_num = data[1]
    today = date.today()

    if date_num == 1:
        time = timedelta(days=7)

    elif date_num == 2:
        time = timedelta(days=14)

    elif date_num == 3:
        time = timedelta(days=30)

    elif date_num == 4:
        time = timedelta(days=60)

    elif date_num == 5:
        time = timedelta(days=180)

    startDate = (today - time).isoformat()
    timeUnit = "date"
    endDate = today.isoformat()

    return (data[0], [startDate, timeUnit, endDate])

def printResult(result: dict) -> None:
    print('===분석결과===')
    print(json.dumps(result, ensure_ascii=False, indent=4))


def main()->None:

    while True:
        menu()
        try:
            user_input=input("숫자를 입력해주세요>")
            user_input=int(user_input)

        except ValueError:
            print('숫자를 입력해주세요')
            continue

        if user_input==1:
            data=UserSearch()
            Filtered_data=dataFilter(data)
            response = naverSearch(Filtered_data)
            ai_reponse = Analysis(response)
            printResult(ai_reponse)
        elif user_input==2:
            print()
            print('프로그램을 종료합니다.')
            return
        
        else:
            print()
            print('범위에 맞는 숫자를 입력해주세요')
            continue

main()