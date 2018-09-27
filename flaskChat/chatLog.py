

class ChatLog(object):
    chatLogStr = ""
    @staticmethod
    def append(string):
        ChatLog.chatLogStr = ChatLog.chatLogStr + string + "\n"
        if len(ChatLog.chatLogStr) > 4:
            ChatLog.chatLogStr = "\n".join(ChatLog.chatLogStr.splitlines()[-4:])


    @staticmethod
    def read():
        #Return last 5 elements
        return ChatLog.chatLogStr