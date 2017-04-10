import logging

from philosopher import Philosopher
from chopsticks import Chopsticks

if __name__ == "__main__":
    logging.basicConfig(format='[%(asctime)s]:%(name)s:%(levelname)s:%(message)s', level=logging.DEBUG)
    log = logging.getLogger(__name__)

    names = ["Puper", "Schultz", "Bados", "Denis", "Fabel"]
    chopsticks = Chopsticks(5)
    philosophers = [Philosopher(name, chopsticks) for name in names]
    threads = [phil.start() for phil in philosophers]
    joins = [phil.join() for phil in philosophers]

    log.info("All done")