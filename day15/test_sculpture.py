from day15.sculpture import Sculpture


def test_time_for_first_capsule_passing_through():
    sculpture = Sculpture(['Disc #1 has 5 positions; at time=0, it is at position 4.',
                           'Disc #2 has 2 positions; at time=0, it is at position 1.'])
    assert sculpture.time_for_first_capsule_passing_through() == 5
