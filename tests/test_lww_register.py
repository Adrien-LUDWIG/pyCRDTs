from pycrdts.lww_register import LWWRegister


class TestLWWRegister:
    def test_create(self) -> None:
        # Given
        lww_register: LWWRegister = LWWRegister(0)

        # Then
        assert lww_register.value() is None
        assert lww_register.timestamp.clock == 0

    def test_assign(self) -> None:
        # Given
        lww_register: LWWRegister = LWWRegister(0)

        # When
        lww_register.assign(42)

        # Then
        assert lww_register.value() == 42
        assert lww_register.timestamp.clock == 1

    def test_merge(self) -> None:
        # Given
        lww_register_1: LWWRegister = LWWRegister(0)
        lww_register_2: LWWRegister = LWWRegister(1)

        # When
        lww_register_1.assign(3)
        lww_register_2.merge(lww_register_1)
        assert lww_register_2.value() == 3
        assert lww_register_2.timestamp.clock == 1

        lww_register_1.assign(14)
        lww_register_1.assign(159)
        assert lww_register_1.value() == 159
        assert lww_register_1.timestamp.clock == 3

        lww_register_2.assign(3)
        assert lww_register_2.value() == 3
        assert lww_register_2.timestamp.clock == 2

        lww_register_1.merge(lww_register_2)
        assert lww_register_1.value() == 159
        assert lww_register_1.timestamp.clock == 3

        lww_register_2.merge(lww_register_1)
        assert (
            lww_register_2.value() == 159
        ), f"lww_register_1: {lww_register_1}, lww_register_2: {lww_register_2}"
        assert lww_register_2.timestamp.clock == 3

    def test_str(self) -> None:
        # Given
        lww_register: LWWRegister = LWWRegister(0)
        assert (
            str(lww_register) == "(Value: None, Timestamp: (Clock: 0, Id: 0))"
        )

        # When
        lww_register.assign(42)

        # Then
        assert str(lww_register) == "(Value: 42, Timestamp: (Clock: 1, Id: 0))"
