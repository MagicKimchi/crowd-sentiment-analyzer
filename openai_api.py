from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
import os

print(__file__)

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

class AnalysisResult(BaseModel):
    trend: str
    concentration: str
    attention_spike: str 

def Analysis(response):

    keyword = response["results"][0]["keywords"][0]
    data = response["results"][0]["data"]
    
    result = client.responses.parse(
        model="gpt-5.6-sol",
        input=[
            {"role": "system", "content": 
                "넌 해당 퍼센트를 보고 추세를 분석하는 분석가이다."
                "ratio는 절대 검색량이나 퍼센트가 아니라, 분석 기간 내 최고 검색 관심도를 100으로 정규화한 상대지수이다. "
                "검색 관심도의 상승·하락 추세, 관심이 집중된 시점, 평소 흐름 대비 급격한 관심 증가 여부만 분석한다. "
                "검색 관심도만으로 주가 상승·하락, 긍정·부정 감정, 매수·매도 의도를 추론하지 않는다."
            },
            {"role": "user", "content": f"{keyword}를 기반으로 {data}안에 있는 모든 퍼센트를 분석해서 추세를 40글자 이내로 분석해줘"}
        ],
        text_format=AnalysisResult
    )

    analysis = result.output_parsed

    final_result = {
        'startDate': response["startDate"],
        'endDate': response['endDate'],
        **analysis.model_dump()
    }

    return final_result

print(AnalysisResult.model_fields.keys())