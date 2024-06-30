from pycrdts.g_set import GSet


class TestGSet:
    def test_add(self):
        # Given
        g_set = GSet()
        assert g_set.payload == set()

        # When
        g_set.add(42)

        # Then
        assert g_set.payload == {42}

    def test_lookup(self):
        # Given
        g_set = GSet()
        g_set.add(42)

        # Then
        assert g_set.lookup(42)
        assert not g_set.lookup(101010)

    def test_compare(self):
        g_set_1 = GSet()
        g_set_2 = GSet()

        # Sets are both empty
        assert g_set_1.compare(g_set_2)
        assert g_set_2.compare(g_set_1)

        # Set 1 is empty, set 2 is not
        g_set_2.add(42)
        assert g_set_1.compare(g_set_2)
        assert not g_set_2.compare(g_set_1)

        # Sets 1 and 2 are different
        g_set_1.add(101010)
        assert not g_set_1.compare(g_set_2)
        assert not g_set_2.compare(g_set_1)

        # Sets 1 is a subset of set 2
        g_set_2.add(101010)
        assert g_set_1.compare(g_set_2)
        assert not g_set_2.compare(g_set_1)

        # Sets 1 and 2 are equal (not empty)
        g_set_1.add(42)
        assert g_set_1.compare(g_set_2)
        assert g_set_2.compare(g_set_1)

    def test_merge(self):
        g_set_1 = GSet()
        g_set_2 = GSet()
        assert g_set_1.payload == set()
        assert g_set_2.payload == set()

        # Sets are both empty
        g_set_1.merge(g_set_2)
        assert g_set_1.payload == set()
        assert g_set_2.payload == set()

        # Set 1 is empty, set 2 is not
        g_set_2.add(42)
        g_set_1.merge(g_set_2)
        assert g_set_1.payload == {42}
        assert g_set_2.payload == {42}

        # Sets 1 and 2 are different
        g_set_1.add(101010)
        g_set_2.add(3)
        g_set_2.merge(g_set_1)
        assert g_set_1.payload == {42, 101010}
        assert g_set_2.payload == {42, 3, 101010}

        # Sets 1 is a subset of set 2
        g_set_1.merge(g_set_2)
        assert g_set_1.payload == {42, 3, 101010}
        assert g_set_2.payload == {42, 3, 101010}

        # Sets 1 and 2 are equal (not empty)
        g_set_1.merge(g_set_2)
        assert g_set_1.payload == {42, 3, 101010}
        assert g_set_2.payload == {42, 3, 101010}

    def test_str(self) -> None:
        g_set = GSet()
        assert str(g_set) == "set()"

        g_set.add(3)
        assert str(g_set) == "{3}"

        g_set.add(14)
        assert str(g_set) == "{3, 14}"
