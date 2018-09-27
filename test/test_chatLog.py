import unittest

from flaskChat.chatLog import ChatLog

class test_ChatLog(unittest.TestCase):
    def setUp(self):
        pass

    def test_append_to_chat(self):
        self.testString = "test"
        ChatLog.append(self.testString)
        self.assertEqual(ChatLog.chatLogStr, self.testString + "\n")

    def test_read_from_chat(self):
        ChatLog.chatLogStr = "line 1\nLine 2\nLine 3\nline 4\nLine 5\nLine 6"
        self.assertEqual(ChatLog.read(), "Line 3\nline 4\nLine 5\nLine 6")