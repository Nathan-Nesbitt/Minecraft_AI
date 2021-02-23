# Import threading since we are running 2 servers
from threading import Thread

# Local Imports
from back_end.broker import Broker

# Jank import for front end module
def import_front_end():
    from front_end import server


def create_broker():
    # Starts the broker
    Broker()


# We have to start the front end in a thread cause flask
# can handle being run in a thread, WS cannot.
front_end = Thread(target=import_front_end)
front_end.start()
# Then we start the broker.
create_broker()
