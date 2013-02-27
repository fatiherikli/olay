from collections import defaultdict

class Dispatcher(object):
    """
    The dispatcher class that allows binding and triggering an event
    """
    def __init__(self):
        self._events = defaultdict(list)

    def on(self, event, callback=None):
        """
        Binds a callback to an event.
        Also supports the decorator way.
        Examples:
            olay.on("hello", callable)
            olay.on("hello")(callable)
        """
        if callback is None:
            def _decorator(callback):
                self.on(event, callback)
            return _decorator

        self._events[event].append(callback)

    def once(self, event, callback):
        """
        Binds a callback for triggering just one time
        """
        callback.once = True
        self.on(event, callback)

    def off(self, event, callback=None):
        """
        Removes a callback from an event if callback is provided,
        otherwise removes all callbacks of the event.
        """
        if callback:
            self._events[event].remove(callback)
        else:
            del self._events[event]

    def trigger(self, event, *args, **kwargs):
        """
        Runs the callbacks of the provided event.
        """
        for callback in self._events[event]:
            callback(*args, **kwargs)
            if getattr(callback, "once", False):
               self.off(event, callback)
