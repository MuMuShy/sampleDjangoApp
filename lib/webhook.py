import logging
import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
from django.conf import settings
logger = logging.getLogger(__name__)

class BaseEventHandler:

    def __init__(self, request):
        #self.api_wrapper = LineBotApiWrapper(self.line_channel_type)
        self.line_api = LineBotApi(settings.CHANNEL_ACCESS_TOKEN)
        self.request = request

    def handle_event(self, event):
        logger.debug('event: {}'.format(json.loads(str(event))))
        line_uid = event.source.user_id

        self.line_api.reply_message(event.reply_token,TextSendMessage("test"))
