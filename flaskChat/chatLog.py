import collections


class ChatLog(object):
    #Using deque makes the chat log first-in-first-out with a fixed max len
    log = collections.deque([""], 5)

    @staticmethod
    def append(msg):
        ChatLog.log.append(msg)


    @staticmethod
    def read():
        #Return last 5 elements
        if len(ChatLog.log) == 0:
            return ""
        return "\n".join(ChatLog.log)+"\n"