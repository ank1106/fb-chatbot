import json
import lxml.html as lh
from lxml.html.clean import clean_html
import requests

class FBCore():
    """Implements FB messenger API for sending message"""

    def __init__(self, page_token):
        """Set page access token """
        self.page_token = page_token


    def sendReply(self, encoded_msg):
        """send message to recipent messenger"""

        url = "https://graph.facebook.com/v3.3/me/messages?access_token={}".format(self.page_token)
        res = requests.post(url , data=json.dumps(encoded_msg), headers={"Content-Type": "application/json"})
        if res.status_code == 200:
            return True
        else:
            return res.text


class FBMessenger(FBCore):
    """Utility class to implement methods to format messages"""

    def stripTags(self, raw_html):
        """
            strip html tags from text  
        """

        t = lh.fromstring(raw_html)
        text = clean_html(t)
        return text.text_content()


    def sendMessage(self, psid, msg):
        res = {
            "recipient":{
                "id":psid
            },
            "message":{
                "text":self.stripTags(msg)
            }
        }
        return self.sendReply(res)
    