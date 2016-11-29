import threading
import time
import unittest

import funker


class HandleTest(unittest.TestCase):
    def test_handle(self):
        def f(x, y):
            return x + y

        threading.Thread(target=funker.handle, args=[f]).start()
        time.sleep(0.1)

        assert funker.call("localhost", x=1, y=2) == 3

    def test_handle_no_return_value(self):
        def f(x):
            return

        threading.Thread(target=funker.handle, args=[f]).start()
        time.sleep(0.1)

        assert funker.call("localhost", x=1) is None
