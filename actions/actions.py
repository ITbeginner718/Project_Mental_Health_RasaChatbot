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


# 현재 파일의 디렉토리 경로를 얻기(절대 경로)
current_dir = os.path.dirname("..\\actions")

# 현재 디렉토리의 상위 디렉토리 경로를 얻기
parent_dir = os.path.dirname(current_dir)
# 상위 디렉토리 경로를 sys.path에 추가
sys.path.append(parent_dir)

import function.func as func

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

# 사용자 발화 예외 처리(자동 호출 )
class ActionDefaultFallback(Action):
    """대화의 이전 상태로 돌아가는 기본 액션을 실행합니다"""

    def name(self) -> Text:
        return "action_default_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:


       # 1. 사용자 질의 가져오기 
        uesrMessage=tracker.latest_message.get('text')
        print(f"Received Message:{uesrMessage}")

        dispatcher.utter_message(template="utter_please_rephrase")

        print("action_default_fallback:bad Request")
        # 대화를 되돌리기 위한 사용자 메시지를 되돌립니다.
        return [UserUtteranceReverted()]



class ActionAskFeeling(Action):
    def name(self):
        return "action_ask_feeling"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        parts = [
            "정말 힘든 시간을 보내고 계시네요.",
            "요즘 어떤 일들 때문에 그렇게 느끼시는 건지, 이야기해주실 수 있을까요?",
            "당신의 마음과 상황을 조금 더 이해하고 싶어요.",
        ]

        # 1. 사용자 질의 가져오기 
        uesrMessage=tracker.latest_message.get('text')
        print(f"Received Message:{uesrMessage}")

        # 각 부분을 순차적으로 전송
        print(f"Send Message to NodeJs:")
        for part in parts:
            print(part)
            dispatcher.utter_message(text=part)

        return []


class ActionReasonStupidSelf(Action):
    def name(self):
        return "action_stupid_self"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        parts = [
            "당신이 그렇게 느끼시는 것에 대해 정말 마음이 아프네요. ",
            "자신을 멍청하다고 생각하고, 잘하는 것이 하나도 없다고 느끼는 감정은 누구에게나 있을 수 있어요.",
            "하지만 그런 생각이 당신의 진짜 가치나 능력을 정확히 반영하지는 않습니다.",
            "각자의 속도와 방식으로 성장하고, 빛나는 순간이 있어요.",
            "우리가 스스로를 너무 엄격하게 판단하게 되면, 진정으로 가진 재능이나 강점을 보지 못하게 되는 경우가 많게 돼요. 당신이 잘하는 것이 분명 있어요.",
            "아마도 그것이 아직 눈에 띄지 않을 수도 있고, 아니면 당신이 그것을 충분히 중요하게 여기지 않았을 수도 있어요.",
        ]

       # 1. 사용자 질의 가져오기 
        uesrMessage=tracker.latest_message.get('text')
        print(f"Received Message form Node: {uesrMessage} \n")

        # 각 부분을 순차적으로 전송
        print(f"Send Message to NodeJs:")
        for part in parts:
            dispatcher.utter_message(text=part)
            print(part)

        return []


class ActionFeedbackStupidSelf(Action):
    def name(self):
        return "action_stupid_self_feedback"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        parts = [
            "비록 별게 아니라고 생각해도 작은 성취들을 축하하고, 자신에게 긍정적인 말을 해보셨으면 좋겠어요.",
            "당신이 좋아하는 것이나 관심 있는 분야에 조금씩 시간을 투자해 보세요. ",
            "자신을 둘러싼 작은 것들에서부터 시작해, 당신이 좋아하는 것과 잘하는 것을 찾아보세요. ",
            "자신에 대해 조금 더 긍정적인 시각을 가지려고 노력하면, 당신의 강점과 재능을 발견할 기회가 더 많아질 거예요.",
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


# class ValidateRestaurantForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_sample_form"

#     @staticmethod
#     def cuisine_db() -> List[Text]:
#         """Database of supported cuisines"""

#         return ["김치찌개", "보쌈", "삼겹살"]

#     #이거 완전 중요함 해당 슬롯에 대한 검증을 할 때는
#     #함수명을  validate_{slot_name} 이렇게 해야함
#     def validate_cuisine(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate cuisine value."""
#         slot_value=str(slot_value)

#         if slot_value.lower() in self.cuisine_db():
#             # validation succeeded, set the value of the "cuisine" slot to value
#             message = f"{slot_value} 좋았어"
#             dispatcher.utter_message(text=message)
#             return {"cuisine": slot_value}
#         else:
#             # validation failed, set this slot to None so that the
#             message=f"뭐~어~!? {slot_value}~? 다른거~"
#             dispatcher.utter_message(text=message)
#             return {"cuisine": None}

#     def validate_number(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,)-> Dict[Text, Any]:

#         """Validate cuisine value."""

#         slot_value= func.extractNumber(slot_value)
#         slot_value= int(slot_value)

#         print(slot_value)

#         if slot_value<3:
#             # validation succeeded, set the value of the "cuisine" slot to value
#             dispatcher.utter_message(text="좋아 딱 그 정도가 좋아")
#             return {"number": slot_value}
#         else:
#             # validation failed, set this slot to None so that the
#             message=f"{slot_value}인분? 안돼 너무 많아.. "
#             dispatcher.utter_message(text=message)
#             return {"number": None}

# class ActionRestart(Action):

#   def name(self) -> Text:
#       return "action_orderFood"

#   async def run(
#       self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
#   ) -> List[Dict[Text, Any]]:


#         # custom behavior

#         cuisine= tracker.get_slot('cuisine')
#         number= tracker.get_slot('number')

#         number= func.extractNumber(number)

#         message = f"{cuisine} {number}인분 나왔다 우리 맛있게 먹자!"
#         dispatcher.utter_message(text=message)

#         return [SlotSet("cuisine", None), SlotSet("number",None)]

# class ActionRestart2(Action):

#   def name(self) -> Text:
#       return "action_reason_number"

#   async def run(
#       self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
#   ) -> List[Dict[Text, Any]]:


#         # custom behavior

#         number_local= tracker.get_slot('number_local')
#         cuisine= tracker.get_slot('cuisine')

#         number_local= func.extractNumber(number_local)

#         message = f"야! 뭔소리야! 나 원래 조금 먹거든?;; {cuisine} {number_local}인분은 너무 많아!"
#         dispatcher.utter_message(text=message)

#         return []
