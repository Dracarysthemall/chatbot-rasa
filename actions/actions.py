# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionProvideInfos(Action):
    def name(self) -> Text:
        return "action_Provide_Infos"
#
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        branche = tracker.get_slot("branche")

        dic = {
            "BDCC"  :   "You asked for bdcc !",
            "GLSID" :   "You asked for glsid!",
            "GIL"   :   "You asked for gil!",
            "GMSI"  :   "You asked for gmsi!",
            "SEER"  :   "You asked for seer!",
            "GECSI" :   "You asked for gecsi!",
            "AOE"   :   "You asked for aoe!",
            "FC"    :   "You asked for fc!",
        }
        if branche not in dic.keys() :
            dispatcher.utter_message(text="sorry!! you have to specify a branche!")
        else:
            dispatcher.utter_message(text=dic[branche])
            
        return []

# class ActionAnswerDate(Action):
#     def name(self) -> Text:
#         return "action_Answer_Date"
# #
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         with open("../date/concours.txt") as f:
#             date = f.read()
#             dispatcher.utter_message(text=date)          
#         return []


