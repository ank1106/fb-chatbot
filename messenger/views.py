from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
import json
from .fb import FBMessenger
from .wiki_api import searchWiki
import os
# token = "EAAGFLdrS7VwBAF9ZB7Mu9xS6wKPlcsnXGlaJ7mKLjZCav2VL3sRuygDVqzg52OorOknyoUWQLwm9fUnFcCznZB8LtcmRGfjfTWnXRV5KKWhykrfKcAjgKZANZBKqsunfLvycX6ZBwLvMGWJZAb1FKlGXoeaEj5ExfESa6mY5xQYZBQZDZD"

class FacebookAPI(APIView):

    def get(self, request):
        """webhook verification reqeuest, returns verification token provided with 
            callback url in FB APP webhook setup
        """
        # token_sent = request.GET.get("hub.verify_token")
        return HttpResponse(request.GET.get('hub.challenge')) 

    def post(self, request):
        """Listens to messages from messenger webhook, replies with wiki search results"""
        
        fb = FBMessenger(os.environ["LONG_ACCESS_TOKEN"])
        output = request.data
        for event in output.get('entry', []):
            messaging = event.get('messaging',[])
            if messaging:
                message = messaging[0]
                query = None
                
                # get the user query from message, quick replies or postbacks
                if message.get("message"):
                    if message['message'].get('text'):
                        query = message['message'].get('text')
                    if message['message'].get('quick_reply'):
                        query = message['message']['quick_reply']["payload"]
                if message.get('postback'):
                    query = message['postback']['title']
                if query:
                    user_id = message['sender']['id']
                    res = searchWiki(query)
                    if res:
                        for item in res:
                            fb.sendMessage(user_id, "{}\n{}\n{}".format(item["title"], item["des"], item["link"]))
                    else:
                        fb.sendMessage(user_id, "Opps! something went wrong")
        
        return JsonResponse({"status":"ok"})
        


