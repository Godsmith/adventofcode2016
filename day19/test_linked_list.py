import pytest

from day19.linked_list import LinkedList


def test_str():
    linked = LinkedList([1, 2, 3])
    assert str(linked) == "[1, 2, 3]"


class TestRemove:
    def test_middle(self):
        linked = LinkedList([1, 2, 3, 4, 5])
        linked.remove(2)
        assert str(linked) == "[1, 2, 4, 5]"

    def test_beginning(self):
        linked = LinkedList([1, 2, 3, 4, 5])
        linked.remove(0)
        assert str(linked) == "[2, 3, 4, 5]"
        assert linked.first.value == 2

    def test_end(self):
        linked = LinkedList([1, 2, 3, 4, 5])
        linked.remove(4)
        assert str(linked) == "[1, 2, 3, 4]"
        assert linked.last.value == 4

    def test_outside(self):
        linked = LinkedList([1, 2, 3, 4, 5])
        with pytest.raises(IndexError):
            linked.remove(5)

    def test_remove_down_to_one(self):
        linked = LinkedList([1, 2])
        linked.remove(1)
        assert linked.first.value == linked.last.value == 1


def test_rotate():
    linked = LinkedList([1, 2, 3, 4, 5])
    assert linked.first.value == 1
    assert linked.last.value == 5
    linked.rotate()
    assert str(linked) == "[2, 3, 4, 5, 1]"
    assert linked.first.value == 2
    assert linked.last.value == 1
