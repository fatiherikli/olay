from collections import defaultdict

class Dispatcher(object):
    """
    The dispatcher class that allows binding and triggering an event
    """
    def __init__(self):
        self._events = defaultdict(list)

    def on(self, event, callback):
        """
        Binds a callback to an event
        """
        self._events[event].append(callback)

    def once(self, event, callback):
        """
        Binds a callback for triggering just one time
        """
        callback.once = True
        self.on(event, callback)

    def off(self, event, callback=None):
        """
        Removes a callback if callback is provided,
        otherwise removes all callbacks.
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
            if hasattr(callback, "once") and callback.once:
               self.off(event, callback)
