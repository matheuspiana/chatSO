import os
from datetime import datetime
from datetime import date

from pubnub.callbacks import SubscribeCallback
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

os.environ["pubsub_uuid"] = "piana-pc"

pnconfig = PNConfiguration()
pnconfig.publish_key = os.getenv("pubsub_pub")
pnconfig.subscribe_key = os.getenv("pubsub_sub")
pnconfig.uuid = os.getenv("pubsub_uuid")

canal = "trabso"

pubnub = PubNub(pnconfig)


class RecebeMensagem(SubscribeCallback):
    def presence(self, pubnub, event):
        pass

    def status(self, pubnub, event):
        pass

    def message(self, pubnub, event):
        data =  datetime.now().strftime("%H:%M:%S")
        user = event.message["usr"]
        mensagem = event.message["msg"]

        if "/" not in mensagem[0]:
            print("[{}] {}: {}".format(data,user, mensagem))
        
        elif mensagem == "/cls":
            os.system('cls')

        elif mensagem == "/quit":
            print(user,"Vazou")
            os._exit(1)
            
        else:
            pass

                

pubnub.add_listener(RecebeMensagem())
pubnub.subscribe().channels(canal).with_presence().execute()
