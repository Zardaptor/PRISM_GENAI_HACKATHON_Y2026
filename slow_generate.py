import json, os, time
from google import genai
from pydantic import BaseModel
from typing import List, Optional

class BaseDeeplink(BaseModel): deeplink: str
class Deeplink(BaseDeeplink): description: str; message: Optional[str] = ''; originalType: Optional[str] = None
class ValidationDeepLink(BaseDeeplink): key: str; resultType: Optional[str] = None; condition: Optional[str] = None; value: Optional[str] = None
class StepGroup(BaseModel): steps: List[str]; validationDeeplink: Optional[ValidationDeepLink] = None; actionableDeeplink: Optional[Deeplink] = None
class Action(BaseModel): actionName: str; description: str; stepGroups: List[StepGroup]; category: Optional[str] = 'manual'
class Goal(BaseModel): goal: str; title: str; actions: List[Action]; score: float
class ContextDeeplinkResponse(BaseModel): contexts: List[Goal] = []

api_key = 'INSERT_YOUR_GEMINI_API_KEY_HERE'
client = genai.Client(api_key=api_key)

base_path = r'C:\Users\suraj\Downloads\Samsung PRISM Gen AI Hackathon 3.0-20260929T181239Z-1-001\Samsung PRISM Gen AI Hackathon 3.0\Theme 2'
siis = json.load(open(os.path.join(base_path, 'siis_responses.json'), encoding='utf-8'))['responses']
deeplinks = json.load(open(os.path.join(base_path, 'deeplinks.json'), encoding='utf-8'))['deeplinks']
deeplinks_str = json.dumps([{'dl': d['deeplink'], 'desc': d['description'], 'msg': d.get('message', '')} for d in deeplinks[:30]])

final_output = []
for i, item in enumerate(siis):
    print(f'Processing {i+1}/20...')
    prompt = f'You are an expert Samsung support agent. Query: {item["original_query"]} KB: {item["siis_response"]} Links: {deeplinks_str} Task: Extract troubleshooting steps matching the schema.'
    for attempt in range(5):
        try:
            response = client.models.generate_content(model='gemini-3.8-flash', contents=prompt, config={'response_mime_type': 'application/json', 'response_schema': ContextDeeplinkResponse})
            final_output.append({'query': item['original_query'], 'response': json.loads(response.text)})
            with open('final_submission.json', 'w') as f:
                json.dump(final_output, f, indent=2)
            print('Success!')
            break
        except Exception as e:
            print('Error:', e)
            time.sleep(20) # Wait out the rate limit
    time.sleep(13) # Keep under 5 RPM

print('Finished!')
