import collections


class ChatLog(object):
    #Using deque makes the chat log first-in-first-out with a fixed max len
    log = collections.deque([""], 5)

    @staticmethod
    def append(msg):
        if msg != "" and msg != "\n":
            ChatLog.log.append(msg)


    @staticmethod
    def read():
        #Return last 5 elements
        return "\n".join(ChatLog.log)