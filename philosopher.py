import random
from threading import Thread
from time import sleep

from chopstick_state import ChopstickState
from philosopher_state import PhilosopherState
import logging


class Philosopher(Thread):

    def __init__(self, name, chopstick_pool):
        self.log = logging.getLogger(name)
        self._eating_time = 5
        self._philosopher_name = name
        self._state = PhilosopherState.thinking
        self._chopstick_pool = chopstick_pool
        self._total_ate_times = 0
        self._total_thought_times = 0
        Thread.__init__(self, name=self.philosopher_name, args=())
        self._my_chopsticks = None
        self.log.debug("created")

    @property
    def philosopher_name(self):
        return self._philosopher_name

    @philosopher_name.setter
    def philosopher_name(self, name):
        self._philosopher_name = name

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def total_ate_times(self):
        return self._total_ate_times

    @total_ate_times.setter
    def total_ate_times(self, value):
        self._total_ate_times = value

    @property
    def total_thought_times(self):
        return self._total_thought_times

    @total_thought_times.setter
    def total_thought_times(self, value):
        self._total_thought_times = value

    @property
    def my_chopsticks(self):
        return self._my_chopsticks

    @my_chopsticks.setter
    def my_chopsticks(self, value):
        self._my_chopsticks = value

    @property
    def chopstick_pool(self):
        return self._chopstick_pool

    @property
    def eating_time(self):
        return self._eating_time

    @eating_time.setter
    def eating_time(self, value):
        pass

    def eat(self):
        self.state = PhilosopherState.eating
        self.total_ate_times += 1
        self.log.info("is eating {} time".format(self.total_ate_times))
        sleep(self.eating_time)
        self.release_chopsticks()

    def think(self):
        self.state = PhilosopherState.thinking
        self.total_thought_times += 1
        self.log.info("is thinking {} time".format(self.total_thought_times))
        sleep(random.randint(1,10))

    def release_chopsticks(self):
        for chopstick in self.my_chopsticks:
            chopstick.state = ChopstickState.free
            chopstick.owner = None
        self.my_chopsticks = None

    def process(self):
        self.log.debug("{} is trying to acquire chopsticks".format(self.philosopher_name))
        self.my_chopsticks = self.chopstick_pool.acquire_pair()
        if self.my_chopsticks:
            self.eat()
        else:
            self.log.debug("{} couldn't acquire chopsticks".format(self.philosopher_name))
            self.think()

    def run(self, cycles=5):
        if cycles is None:
            while True:
                self.process()
        else:
            while self._total_ate_times < cycles:
                self.process()

        self.log.info("{} ate {} times and thought {} times".format(self.name, self._total_ate_times, self._total_thought_times))
