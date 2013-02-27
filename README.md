Backbone like events in Python

#### Example

    from olay import olay

    @olay.on("registration:success")
    def registration_success(username):
        print username, "Registration successfully completed"

    olay.trigger("registration:success", username="fatiherikli")


#### olay.on

Binds a callback to an event. Also supports the decorator way.

    olay.on("hello", callable)
    olay.on("hello")(callable)

#### olay.trigger

Runs the callbacks of the provided event. Supports arguments and keyword arguments for callback functions.

    olay.trigger("hello")
    olay.trigger("hello", 1, 2, username="test")

#### olay.once

Binds a callback for triggering just one time.

    olay.once("hello", callable)
    olay.trigger("hello") // worked
    olay.trigger("hello") // not worked

#### olay.off

Removes a callback from an event if callback is provided, otherwise removes all callbacks of the event.

    olay.off("hello")
    olay.off("hello", callback)

### Using different dispatcher instance

You can use your dispatcher instance rather then global `olay` instance.

    from olay import Dispatcher

    dispatcher = Dispatcher()
    dispatcher.on("hello", callback)

