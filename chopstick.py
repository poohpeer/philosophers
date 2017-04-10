from chopstick_state import ChopstickState


class Chopstick(object):

    def __init__(self):
        self._state = ChopstickState.free
        self._owner = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner
