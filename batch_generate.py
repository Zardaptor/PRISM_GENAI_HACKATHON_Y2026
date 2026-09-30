import json
import os
from google import genai
from pydantic import BaseModel
from typing import List, Optional, Dict
from enum import Enum

class Condition(str, Enum): greater, equal, less = 'greater', 'equal', 'less'
class ResultTypes(str, Enum): boolean, intNum, string, floatNum = 'boolean', 'integer', 'str', 'float'
class actionCategory(str, Enum): auto, manual, critical = 'auto', 'manual', 'critical'
class BaseDeeplink(BaseModel): deeplink: str
class Deeplink(BaseDeeplink): description: str; message: Optional[str] = ''; originalType: Optional[str] = None
class ValidationDeepLink(BaseDeeplink): key: str; resultType: Optional[ResultTypes] = None; condition: Optional[Condition] = None; value: Optional[str] = None
class StepGroup(BaseModel): steps: List[str]; validationDeeplink: Optional[ValidationDeepLink] = None; actionableDeeplink: Optional[Deeplink] = None
class Action(BaseModel): actionName: str; description: str; stepGroups: List[StepGroup]; category: Optional[actionCategory] = actionCategory.manual
class Goal(BaseModel): goal: str; title: str; actions: List[Action]; score: float
class ContextDeeplinkResponse(BaseModel): contexts: List[Goal] = []

api_key = 'INSERT_YOUR_GEMINI_API_KEY_HERE'
client = genai.Client(api_key=api_key)

base_path = r'C:\Users\suraj\Downloads\Samsung PRISM Gen AI Hackathon 3.0-20260929T181239Z-1-001\Samsung PRISM Gen AI Hackathon 3.0\Theme 2'
siis = json.load(open(os.path.join(base_path, 'siis_responses.json'), encoding='utf-8'))['responses']
deeplinks = json.load(open(os.path.join(base_path, 'deeplinks.json'), encoding='utf-8'))['deeplinks']
deeplinks_str = json.dumps([{'dl': d['deeplink'], 'desc': d['description'], 'msg': d.get('message', '')} for d in deeplinks[:50]])

final_output = []
print(f'Starting batch generation for {len(siis)} queries...')
for i, item in enumerate(siis):
    print(f'Processing query {i+1}/{len(siis)}...')
    prompt = f'''
    You are an expert Samsung (TechCorp) support agent. 
    Customer Query: "{item['original_query']}"
    Raw Tech Support KB (SIIS Response): {item['siis_response']}
    Available Deep Links for the device: {deeplinks_str}
    Extract the troubleshooting steps from the KB text into the JSON schema. Use the deep links if relevant.
    '''
    try:
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=prompt,
            config={'response_mime_type': 'application/json', 'response_schema': ContextDeeplinkResponse, 'temperature': 0.1}
        )
        final_output.append({'query': item['original_query'], 'response': json.loads(response.text)})
    except Exception as e:
        print('Error on', i, e)

with open('C:\\Users\\suraj\\Desktop\\Projects\\samsung_theme2_app\\final_submission.json', 'w') as f:
    json.dump(final_output, f, indent=2)
print('Generation complete! Saved to final_submission.json')
