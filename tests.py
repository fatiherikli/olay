import unittest

from olay import Dispatcher


class DispatcherTests(unittest.TestCase):

    def setUp(self):
        self.olay = Dispatcher()

    def test_binding(self):
        noop = lambda: None
        self.olay.on("hello", noop)
        events = self.olay._events
        self.assertIn("hello", events)
        self.assertIn(noop, events["hello"])
        self.olay.on("hello", noop)
        self.assertEqual(len(events["hello"]), 2)

    def test_once_binding(self):
        noop = lambda: None
        self.olay.once("hello", noop)
        self.assertTrue(noop.once)

    def test_triggering(self):
        class _test: foo = 0
        def _callback():
            _test.foo += 1
        self.olay.on("hello", _callback)
        self.assertEqual(_test.foo, 0)
        self.olay.trigger("hello")
        self.assertTrue(_test.foo, 1)
        self.olay.trigger("hello")
        self.assertTrue(_test.foo, 2)

    def test_once_triggering(self):
        class _test: foo = 0
        def _callback():
            _test.foo += 1
        self.olay.once("hello", _callback)
        self.assertEqual(_test.foo, 0)
        self.olay.trigger("hello")
        self.olay.trigger("hello")
        self.assertTrue(_test.foo, 1)

    def test_unbinding(self):
        from copy import copy
        class _test: foo = 0
        def _callback():
            _test.foo += 1
        self.olay.on("hello", _callback)
        self.olay.trigger("hello")
        self.assertEqual(_test.foo, 1)
        self.olay.off("hello")
        self.olay.trigger("hello")
        self.assertEqual(_test.foo, 1)
        self.olay.on("hello", _callback)
        self.olay.on("hello", copy(_callback))
        self.olay.trigger("hello")
        self.assertEqual(_test.foo, 3)
        self.olay.off("hello", _callback)
        self.olay.trigger("hello")
        self.assertEqual(_test.foo, 4)

    def test_decorator(self):
        noop = lambda: None
        self.olay.on("hello")(noop)
        events = self.olay._events
        self.assertIn("hello", events)
        self.assertIn(noop, events["hello"])


if __name__ == "__main__":
    unittest.main()
