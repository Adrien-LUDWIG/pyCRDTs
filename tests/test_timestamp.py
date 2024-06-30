from pycrdts.utils.timestamp import Timestamp


class TestTimestamp:
    def test_increment(self) -> None:
        # Given
        id = 0
        timestamp = Timestamp(id)

        # When
        timestamp.tick(id)

        # Then
        assert timestamp.clock == 1
        assert timestamp.id == 0

    def test_compare(self) -> None:
        # Given
        id_1 = 0
        id_2 = 1
        timestamp_1 = Timestamp(id_1)
        timestamp_2 = Timestamp(id_2)

        # Clock is equal to other and id is less
        assert timestamp_1.compare(timestamp_2)

        # Clock is equal to other and id is greater
        assert not timestamp_2.compare(timestamp_1)

        # Clock is less than other
        timestamp_1.tick(id_1)
        assert timestamp_2.compare(timestamp_1)

        # Clock is greater than other
        assert not timestamp_1.compare(timestamp_2)

        # Clock is equal to other and id is equal
        timestamp_1.id = timestamp_2.id
        timestamp_1.clock = timestamp_2.clock
        assert timestamp_1.compare(timestamp_2)
        assert timestamp_2.compare(timestamp_1)

    def test_merge(self) -> None:
        # Given
        id_1 = 0
        id_2 = 1
        timestamp_1 = Timestamp(id_1)
        timestamp_2 = Timestamp(id_2)

        # Clock is equal to other and id is less
        timestamp_1.merge(timestamp_2)
        assert timestamp_1.clock == 0
        assert timestamp_1.id == 1

        # Clock is equal to other and id is greater
        timestamp_2.merge(timestamp_1)
        assert timestamp_2.clock == 0
        assert timestamp_2.id == 1

        # Clock is greater than other
        timestamp_2.tick(id_2)
        timestamp_2.merge(timestamp_1)
        assert timestamp_2.clock == 1
        assert timestamp_2.id == 1
        assert timestamp_1.clock == 0
        assert timestamp_1.id == 1

        # Clock is less than other
        timestamp_1.merge(timestamp_2)
        assert timestamp_1.clock == 1
        assert timestamp_1.id == 1

        # Clock is equal to other and id is equal
        timestamp_1.merge(timestamp_2)
        assert timestamp_1.clock == 1
        assert timestamp_1.id == 1
        assert timestamp_2.clock == 1
        assert timestamp_2.id == 1
        timestamp_2.merge(timestamp_1)
        assert timestamp_2.clock == 1
        assert timestamp_2.id == 1
        assert timestamp_1.clock == 1
        assert timestamp_1.id == 1

    def test_str(self) -> None:
        # Given
        timestamp = Timestamp(0)
        assert str(timestamp) == "(Clock: 0, Id: 0)"

        # When
        timestamp.id = 14
        timestamp.clock = 3

        # Then
        assert str(timestamp) == "(Clock: 3, Id: 14)"
