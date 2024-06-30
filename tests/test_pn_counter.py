from pycrdts.pn_counter import PNCounter


class TestPNCounter:
    def test_increment(self):
        # Given
        pn_counter = PNCounter(1, 0)
        assert pn_counter.value() == 0

        # When
        pn_counter.increment()

        # Then
        assert pn_counter.value() == 1

    def test_decrement(self):
        # Given
        pn_counter = PNCounter(1, 0)
        assert pn_counter.value() == 0

        # When
        pn_counter.increment()

        # Then
        assert pn_counter.value() == 1

    def test_merge(self):
        # Given
        pn_counter1 = PNCounter(2, 0)
        pn_counter1.increment()
        pn_counter1.decrement()
        pn_counter1.decrement()
        pn_counter2 = PNCounter(2, 1)
        pn_counter2.increment()
        pn_counter2.increment()
        pn_counter2.increment()
        pn_counter2.decrement()
        assert not pn_counter1.compare(pn_counter2)
        assert not pn_counter2.compare(pn_counter1)
        assert pn_counter1.value() == -1
        assert pn_counter2.value() == 2

        # When
        pn_counter1.merge(pn_counter2)

        # Then
        assert pn_counter1.value() == 1
        assert pn_counter2.value() == 2
        assert not pn_counter1.compare(pn_counter2)
        assert pn_counter2.compare(pn_counter1)

    def test_str(self) -> None:
        # Given
        pn_counter = PNCounter(1, 0)
        assert str(pn_counter) == "0"

        # When positive
        pn_counter.increment()
        assert str(pn_counter) == "1"

        # When negative
        pn_counter.decrement()
        pn_counter.decrement()
        assert str(pn_counter) == "-1"
