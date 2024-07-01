from pycrdts.pn_counter import PNCounter


class TestPNCounter:
    def test_increment(self):
        # Given
        pn_counter = PNCounter()
        assert pn_counter.value() == 0

        # When
        pn_counter.increment()

        # Then
        assert pn_counter.value() == 1

    def test_decrement(self):
        # Given
        pn_counter = PNCounter()
        assert pn_counter.value() == 0

        # When
        pn_counter.increment()

        # Then
        assert pn_counter.value() == 1

    def test_merge(self):
        # Given
        pn_counter1 = PNCounter()
        pn_counter1.increment()
        pn_counter1.decrement()
        pn_counter1.decrement()
        pn_counter2 = PNCounter()
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
        pn_counter = PNCounter()
        assert str(pn_counter) == "Positive: {}, Negative: {}"

        # When positive
        pn_counter.increment()
        assert (
            str(pn_counter)
            == "Positive: "
            + str({pn_counter.positive_counter.id: 1})
            + ", Negative: {}"
        )

        # When negative
        pn_counter.decrement()
        pn_counter.decrement()
        assert str(pn_counter) == "Positive: " + str(
            {pn_counter.positive_counter.id: 1}
        ) + ", Negative: " + str({pn_counter.negative_counter.id: 2})
