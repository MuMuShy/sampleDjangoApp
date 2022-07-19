from django.conf import settings


class BaseLineChannel:
    secret = None
    access_token = None
    type = None

    def __init__(self, secret, access_token):
        self.secret = secret
        self.access_token = access_token

    @classmethod
    def create(cls, channel_type):
        klass = {
            'client': ClientLineChannel,
        }[channel_type]
        return klass()


class ClientLineChannel(BaseLineChannel):
    type = 'client'

    def __init__(self):
        super().__init__(settings.CHANNEL_SECRET,
                         settings.CHANNEL_ACCESS_TOKEN)