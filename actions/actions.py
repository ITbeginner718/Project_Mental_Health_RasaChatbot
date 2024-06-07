# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

import sys
import os
import yaml

# 현재 파일의 디렉토리 경로를 얻기(절대 경로)
current_dir = os.path.dirname("..\\actions")

# 현재 디렉토리의 상위 디렉토리 경로를 얻기
parent_dir = os.path.dirname(current_dir)
# 상위 디렉토리 경로를 sys.path에 추가
sys.path.append(parent_dir)

# YAML 파일 로드(피드백)
with open('actions\\feedback.yml', 'r', encoding='utf-8') as file:
    yaml_feedback_data = yaml.safe_load(file)

import function.func as func

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

#오늘의 생각 바꾸기
CHANGE="change"

#키워드 사용
FEEDBACK_CODE=""

# # 사용자 발화 예외 처리(자동 호출 )
# class ActionDefaultFallback(Action):
#     """대화의 이전 상태로 돌아가는 기본 액션을 실행합니다"""

#     def name(self) -> Text:
#         return "action_default_fallback"

#     async def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:


#        # 1. 사용자 질의 가져오기 
#         uesrMessage=tracker.latest_message.get('text')
#         print(f"Received Message:{uesrMessage}")

#         dispatcher.utter_message(response="utter_please_rephrase")

#         print("action_default_fallback:bad Request")

#         intent = tracker.latest_message['intent'].get('name')
#         confidence = tracker.latest_message['intent'].get('confidence')

#         # 사용자에게 의도와 신뢰도를 메시지로 전송
#         message = f"의도: {intent}, 신뢰도: {confidence:.2f}"

#         print(message)
#         # 대화를 되돌리기 위한 사용자 메시지를 되돌립니다.
#         return []
    
####################################인지행동치료 적용 #########################

#######################story_SneeringToMe_situation
class ActionStory_SneeringToMe(Action):
    def name(self):
        return "action_story_SneeringToMe"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):

        # 사용자 이름 가져오기
        username = tracker.get_slot('username')

        intent = tracker.latest_message['intent'].get('name')
        confidence = tracker.latest_message['intent'].get('confidence')

        # 사용자에게 의도와 신뢰도를 메시지로 전송
        message = f"의도: {intent}, 신뢰도: {confidence:.2f}"
        print(message)  
        parts = [
            f"{username}님이 그렇게 느끼시는 것에 대해 정말 마음이 아프네요. ",
            "혹시 어떤 일이 있었는지 이야기해주실 수 있을까요?",  
            f"{username}님의 마음과 상황을 조금 더 이해하고 싶어요.",    
        ]



        # 1. 사용자 질의 가져오기 
        uesrMessage=tracker.latest_message.get('text')
        print(f"Received Message from NodsJS:{uesrMessage}")

        # 각 부분을 순차적으로 전송
        print(f"Send Message to NodeJs:")
        for part in parts:
            dispatcher.utter_message(text=part)
            print(part)
        
                
        # 초기화
        global FEEDBACK_CODE
        FEEDBACK_CODE=""

        return []
    
class ActionStory_SneeringToMe_situation(Action):
    def name(self):
        return "action_story_SneeringToMe_situation"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):

        # 사용자 이름 가져오기
        username = tracker.get_slot('username')
        parts = [
            "그런 생각을 하고 계시군요ㅠ 발표할 때 사람들의 시선을 두려워하는 감정을 느끼는 것은 정말 견뎌내기 힘든 감정입니다.",
            f"제가 {username}님한테 질문을 한 번 드려볼께요",  
            f"혹시 {username}님은 누군가가 발표를 하다가 버벅이면 그 사람을 비판하거나 무시하나요?",    
        ]

        # 1. 사용자 질의 가져오기 
        uesrMessage=tracker.latest_message.get('text')
        print(f"Received Message from NodsJS:{uesrMessage}")

        # 각 부분을 순차적으로 전송
        print(f"Send Message to NodeJs:")
        for part in parts:
            dispatcher.utter_message(text=part)
            print(part)

        return []
    
class ActionStory_SneeringToMe_response1_1(Action):
    def name(self):
        return "action_story_SneeringToMe_response1_1"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):

        # 사용자 이름 가져오기
        username = tracker.get_slot('username')
        parts = [
           f"맞아요. {username}님은 다른 사람이 발표할 때 그런 생각을 하고 계시지 않아요.",
           f"우리 생각을 한 번 바꿔봐요. {username}님이 그렇게 생각하지 않는다면 다른 사람들도 그렇게 생각하지 안하지 않을까요?",
           f"다른 사람들도 {username}님과 같이 그런 마음을 가지지 않았다고 믿어보는 것이 어떨까요?"
        ]

        # 1. 사용자 질의 가져오기 
        uesrMessage=tracker.latest_message.get('text')
        print(f"Received Message from NodsJS:{uesrMessage}")

        # 각 부분을 순차적으로 전송
        print(f"Send Message to NodeJs:")
        for part in parts:
            dispatcher.utter_message(text=part)
            print(part)

        return []


class ActionStory_SneeringToMe_response2_1(Action):
    def name(self):
        return "action_story_SneeringToMe_response2_1"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        # 사용자 이름 가져오기
        username = tracker.get_slot('username')
        parts = [
           f"사람들이 {username}님을 발표하다 실수있다고 비난할 것 같은 느낌이 나는 이유는 대부분 내 마음속의 불안에서 비롯된 거예요",
           "\"나는 완벽하게 해야하는데 그러지 못하면 어떡하지?\" \"나는 무조건 사람들한테 인정받아야 하는데 그러지 못하면 어떡하지?\" 이런 마음에서 말이죠."
           "이런 마음에서 말이죠. 그렇지만 대부분의 사람들은 당신을 평가하는 것이 아닌, 단지 잘 해내기를 바라고 있을 겁니다.",
           "혹여나 발표 도중 실수를 하더라도 절대 비난 받을 일이 아닙니다. 당연히 발생할 수 있는 상황이라고 생각해요.",
           "오늘의 피드백을 받아보시겠어요?(좋아 피드백 해줘 / 괜찮아)"
        ]

        global FEEDBACK_CODE
        FEEDBACK_CODE="0_1"

        # 1. 사용자 질의 가져오기 
        uesrMessage=tracker.latest_message.get('text')
        print(f"Received Message from NodsJS:{uesrMessage}")

        # 각 부분을 순차적으로 전송
        print(f"Send Message to NodeJs:")
        for part in parts:
            dispatcher.utter_message(text=part)
            print(part)
        
        return []

class ActionStory_SneeringToMe_Feedback(Action):
    def name(self):
        return "action_story_SneeringToMe_feedback"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):

        global FEEDBACK_CODE

        # 1. 피드백 데이터 가져오기  
        feedback = yaml_feedback_data['feedback'][FEEDBACK_CODE]

        dispatcher.utter_message(text="네 잠깐만요. 피드백을 받아오겠습니다.") 

        #데이터 전송
        message = f"{CHANGE}@a{feedback}"
        dispatcher.utter_message(text=message)

        FEEDBACK_CODE=""

        #이름 초기화
        return [SlotSet("username", None)]  
