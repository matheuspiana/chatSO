import os
from datetime import datetime


from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

os.environ["pubsub_uuid"] = "piana-pc"

pnconfig = PNConfiguration()
pnconfig.publish_key = os.getenv("pubsub_pub")
pnconfig.subscribe_key = os.getenv("pubsub_sub")
pnconfig.uuid = os.getenv("pubsub_uuid")

canal = "trabso"
usr = input("Seu nome: ")
os.system('cls')
comandos = ["/quit","/date","/help"]

pubnub = PubNub(pnconfig)

while True:
    print("---------------- Chat ---------------")
    print("Digite /help para a lista de comandos")
    msg = input(usr+": ")
    
    envelope = pubnub.publish().channel(canal).message({"msg": msg, "usr": usr}).sync()
    os.system('cls')

    if "/" in msg[0] and msg not in comandos:
        print("Comando inexistente")


    elif msg == comandos[0]:
        os._exit(1)
    
    elif msg == comandos[1]:
        data = datetime.now()
        print ("Data: ",data.day,"/",data.month,"/",data.year)
    
    elif msg == comandos[2]:
        print("------Comandos------")
        print("/quit - Fecha o App\n/date - Mostra a data\n/cls - Limpa o chat")
        

    

    if envelope.status.is_error():
        print("->>>>> DEU PAU")
