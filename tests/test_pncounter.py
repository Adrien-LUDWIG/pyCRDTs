from pycrdts.pncounter import PNCounter


class TestPNCounter:
    def test_increment(self):
        # Given
        pncounter = PNCounter(1, 0)
        assert pncounter.value() == 0

        # When
        pncounter.increment()

        # Then
        assert pncounter.value() == 1

    def test_decrement(self):
        # Given
        pncounter = PNCounter(1, 0)
        assert pncounter.value() == 0

        # When
        pncounter.increment()

        # Then
        assert pncounter.value() == 1

    def test_merge(self):
        # Given
        pncounter1 = PNCounter(2, 0)
        pncounter1.increment()
        pncounter1.decrement()
        pncounter1.decrement()
        pncounter2 = PNCounter(2, 1)
        pncounter2.increment()
        pncounter2.increment()
        pncounter2.increment()
        pncounter2.decrement()
        assert not pncounter1.compare(pncounter2)
        assert not pncounter2.compare(pncounter1)
        assert pncounter1.value() == -1
        assert pncounter2.value() == 2

        # When
        pncounter1.merge(pncounter2)

        # Then
        assert pncounter1.value() == 1
        assert pncounter2.value() == 2
        assert not pncounter1.compare(pncounter2)
        assert pncounter2.compare(pncounter1)
