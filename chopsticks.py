import logging
from chopstick import Chopstick
from chopstick_state import ChopstickState


class Chopsticks(object):
    def __init__(self, chopstick_num):
        self._chopsticks = [Chopstick() for i in range(0, chopstick_num)]
        self.log = logging.getLogger(__name__)
        self.log.debug("Initialized {} chopsticks".format(len(self.chopsticks)))

    @property
    def chopsticks(self):
        return self._chopsticks

    def acquire_pair(self):
        free_chops = []

        # Try to acquire chopstick pair
        for chopstick in self.chopsticks:
            if chopstick.state == ChopstickState.free:
                chopstick.state = ChopstickState.busy
                free_chops.append(chopstick)

            # Return if pair found
            if len(free_chops) == 2:
                return free_chops

        # If here, there is no pair. Release acquired chopsticks, if any.
        for chopstick in free_chops:
            chopstick.state = ChopstickState.free
        return None
