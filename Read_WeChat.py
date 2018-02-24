from win32com.client import constants
import pyttsx3
import win32com.client
import pythoncom
import itchat, time
from itchat.content import *

engine = pyttsx3.init()

@itchat.msg_register(TEXT)
def _(msg):
    # equals to print(msg['FromUserName'])
    print(msg.fromUserName)


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    text = '好友%s说: %s' % (msg.User.RemarkName, msg.text)
    print(text)
    engine.say(text)
    engine.setProperty('volume', 0.9)
    engine.runAndWait()
    #msg.user.send('%s: %s' % (msg.type, msg.text))

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')


itchat.auto_login(True)
itchat.run(True)
