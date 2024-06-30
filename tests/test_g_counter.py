from pycrdts.g_counter import GCounter


class TestGCounter:
    def test_increment(self):
        # Given
        g_counter = GCounter(1, 0)
        assert g_counter.value() == 0

        # When
        g_counter.increment()

        # Then
        assert g_counter.value() == 1

    def test_merge(self):
        # Given
        g_counter1 = GCounter(2, 0)
        g_counter1.increment()
        g_counter2 = GCounter(2, 1)
        g_counter2.increment()

        # When
        assert not g_counter1.compare(g_counter2)
        assert not g_counter2.compare(g_counter1)
        g_counter1.merge(g_counter2)

        # Then
        assert g_counter1.value() == 2
        assert g_counter2.value() == 1
        assert not g_counter1.compare(g_counter2)
        assert g_counter2.compare(g_counter1)

    def test_str(self) -> None:
        # Given
        g_counter = GCounter(1, 0)
        assert str(g_counter) == "0"

        # When
        g_counter.increment()

        # Then
        assert str(g_counter) == "1"
