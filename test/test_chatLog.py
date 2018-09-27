import unittest

from flaskChat.chatLog import ChatLog

class test_ChatLog(unittest.TestCase):
    def setUp(self):
        self.testString = "test"
        self.largeTestString = "test\ntest\ntest\ntest\ntest\ntest\ntest\ntest"

    def test_append_to_chat(self):
        ChatLog.append(self.largeTestString)
        self.assertEqual(ChatLog.chatLogStr, "test\ntest\ntest\ntest")

    def test_read_from_chat(self):
        ChatLog.chatLogStr = self.testString
        self.assertEqual(ChatLog.read(), self.testString)