import threading
import time
import unittest

import funker


class HandleTest(unittest.TestCase):
    def test_handle(self):
        def f(x, y):
            return x + y

        th = threading.Thread(target=funker.handle, args=[f])
        th.daemon = True
        th.start()

        time.sleep(0.1)

        assert funker.call("localhost", x=1, y=2) == 3
