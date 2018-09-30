import unittest
import collections

from flaskChat.chatLog import ChatLog

class test_ChatLog(unittest.TestCase):
    def setUp(self):
        self.testString = "test"
        ChatLog.log.clear()
    def test_append_to_chat(self):
        for i in range(10):
            ChatLog.append(self.testString + str(i))
        self.assertEqual(ChatLog.read(), "test5\ntest6\ntest7\ntest8\ntest9")

    def test_read_from_chat(self):
        ChatLog.log = collections.deque(["foo", "bar"])
        self.assertEqual(ChatLog.read(), "foo\nbar")

    def test_read_empty_log(self):
        self.assertEqual(ChatLog.read(), "")

    def test_add_empty_msg(self):
        ChatLog.append("foo")
        ChatLog.append("")
        ChatLog.append("bar")
        self.assertEqual(ChatLog.read(), "foo\nbar")

    def test_add_newline(self):
        ChatLog.append("foo")
        ChatLog.append("\n")
        ChatLog.append("bar")
        self.assertEqual(ChatLog.read(), "foo\nbar")