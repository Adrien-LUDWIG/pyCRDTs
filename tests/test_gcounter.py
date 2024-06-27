from pycrdts.gcounter import GCounter


class TestGCounter:
    def test_increment(self):
        # Given
        gcounter = GCounter(1, 0)
        assert gcounter.value() == 0

        # When
        gcounter.increment()

        # Then
        assert gcounter.value() == 1

    def test_merge(self):
        # Given
        gcounter1 = GCounter(2, 0)
        gcounter1.increment()
        gcounter2 = GCounter(2, 1)
        gcounter2.increment()

        # When
        assert not gcounter1.compare(gcounter2)
        assert not gcounter2.compare(gcounter1)
        gcounter1.merge(gcounter2)

        # Then
        assert gcounter1.value() == 2
        assert gcounter2.value() == 1
        assert not gcounter1.compare(gcounter2)
        assert gcounter2.compare(gcounter1)
