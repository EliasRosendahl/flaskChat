

class ChatLog(object):
    chatLogStr = ""
    @staticmethod
    def append(string):
        ChatLog.chatLogStr = ChatLog.chatLogStr + string + "\n"

    @staticmethod
    def read():
        #Return last 5 elements
        return "\n".join(ChatLog.chatLogStr.splitlines()[-4:])