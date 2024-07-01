from pycrdts.g_counter import GCounter


class TestGCounter:
    def test_increment(self):
        # Given
        g_counter = GCounter()
        assert g_counter.value() == 0

        # When
        g_counter.increment()

        # Then
        assert g_counter.value() == 1

    def test_merge(self):
        # Given
        g_counter1 = GCounter()
        g_counter1.increment()
        g_counter2 = GCounter()
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
        g_counter = GCounter()
        assert str(g_counter) == "{}"

        # When
        g_counter.increment()

        # Then
        assert str(g_counter) == str({g_counter.id: 1})
