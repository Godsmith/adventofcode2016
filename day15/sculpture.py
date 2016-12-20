from day15.capsule import Capsule
from day15.disc import Disc


class Sculpture:
    def __init__(self, disc_strings):
        self._discs = [Disc.from_string(s) for s in disc_strings]
        self._capsules = []

    def time_for_first_capsule_passing_through(self):
        t = 0
        while True:
            self._evaluate_discs()
            if self._time_for_capsule_that_has_passed_last_disc():
                return self._time_for_capsule_that_has_passed_last_disc()
            self._drop_capsule(t)

            self._tick()
            t += 1

    def _drop_capsule(self, t):
        self._capsules.append(Capsule(starting_time=t))

    def _evaluate_discs(self):
        for disc in self._discs:
            for capsule in self._capsules:
                if disc.location == capsule.location and not disc.open:
                    self._capsules.remove(capsule)

    def _time_for_capsule_that_has_passed_last_disc(self):
        if len(self._capsules) == 0:
            return False
        if self._capsules[-1].location == len(self._discs) + 1:
            return self._capsules[-1].starting_time

    def _tick(self):
        for disc in self._discs:
            disc.tick()
        for capsule in self._capsules:
            capsule.tick()
