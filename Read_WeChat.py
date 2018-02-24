from win32com.client import constants
import pyttsx3
import win32com.client
import pythoncom
import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    text = (msg['Text'])
    print(text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.setProperty('volume', 1)
    engine.runAndWait()


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=True, hotReload=True)
    itchat.run()

