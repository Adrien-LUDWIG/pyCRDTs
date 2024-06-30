from pycrdts.two_phase_set import TwoPhaseSet


class TestTwoPhaseSet:
    def test_add(self):
        # Empty set
        two_phase_set = TwoPhaseSet()
        assert two_phase_set.add_set.payload == set()
        assert two_phase_set.remove_set.payload == set()

        # Adding an element to the set
        two_phase_set.add(42)
        assert two_phase_set.add_set.payload == {42}
        assert two_phase_set.remove_set.payload == set()

        # Adding the same element again has no effect
        two_phase_set.add(42)
        assert two_phase_set.add_set.payload == {42}
        assert two_phase_set.remove_set.payload == set()

    def test_remove(self):
        # Empty set
        two_phase_set = TwoPhaseSet()
        assert two_phase_set.add_set.payload == set()
        assert two_phase_set.remove_set.payload == set()

        # Removing an element that is not in the set has no effect
        two_phase_set.remove(42)
        assert two_phase_set.add_set.payload == set()
        assert two_phase_set.remove_set.payload == set()

        # Removing an element that is in the set
        two_phase_set.add(42)
        two_phase_set.remove(42)
        assert two_phase_set.add_set.payload == {42}
        assert two_phase_set.remove_set.payload == {42}

        # Removing the same element again has no effect
        two_phase_set.remove(42)
        assert two_phase_set.add_set.payload == {42}
        assert two_phase_set.remove_set.payload == {42}

    def test_lookup(self):
        # Empty set
        two_phase_set = TwoPhaseSet()
        assert not two_phase_set.lookup(42)

        # Element is in the set
        two_phase_set.add(42)
        assert two_phase_set.lookup(42)

        # Element has been removed
        two_phase_set.remove(42)
        assert not two_phase_set.lookup(42)

    def test_compare(self):
        # Sets are both empty
        two_phase_set_1 = TwoPhaseSet()
        two_phase_set_2 = TwoPhaseSet()
        assert two_phase_set_1.compare(two_phase_set_2)
        assert two_phase_set_2.compare(two_phase_set_1)

        # Set 1 is empty, set 2 is not
        two_phase_set_2.add(42)
        assert two_phase_set_1.compare(two_phase_set_2)
        assert not two_phase_set_2.compare(two_phase_set_1)

        # Set 1 is empty, set 2 is *seemingly* empty
        two_phase_set_2.remove(42)
        assert two_phase_set_1.compare(two_phase_set_2)
        assert not two_phase_set_2.compare(two_phase_set_1)

        # Set 1 is has the removed element from set 2
        two_phase_set_1.add(42)
        assert two_phase_set_1.compare(two_phase_set_2)
        assert not two_phase_set_2.compare(two_phase_set_1)

        # Set 1 and 2 are *seemingly* empty
        two_phase_set_1.remove(42)
        assert two_phase_set_1.compare(two_phase_set_2)
        assert two_phase_set_2.compare(two_phase_set_1)

        # Set 1 now has a new element
        two_phase_set_1.add(101010)
        assert not two_phase_set_1.compare(two_phase_set_2)
        assert two_phase_set_2.compare(two_phase_set_1)

    def test_merge(self):
        # Sets are both empty
        two_phase_set_1 = TwoPhaseSet()
        two_phase_set_2 = TwoPhaseSet()
        assert two_phase_set_1.add_set.payload == set()
        assert two_phase_set_1.remove_set.payload == set()
        assert two_phase_set_2.add_set.payload == set()
        assert two_phase_set_2.remove_set.payload == set()

        # Merge empty set into empty set has no effect
        two_phase_set_1.merge(two_phase_set_2)
        assert two_phase_set_1.add_set.payload == set()
        assert two_phase_set_1.remove_set.payload == set()
        assert two_phase_set_2.add_set.payload == set()
        assert two_phase_set_2.remove_set.payload == set()

        # Set 1 is empty, set 2 is not
        two_phase_set_2.add(42)
        two_phase_set_1.merge(two_phase_set_2)
        assert two_phase_set_1.add_set.payload == {42}
        assert two_phase_set_1.remove_set.payload == set()
        assert two_phase_set_2.add_set.payload == {42}
        assert two_phase_set_2.remove_set.payload == set()

        # Set 1 is *seemingly* empty, set 2 is not
        two_phase_set_1.remove(42)
        two_phase_set_2.merge(two_phase_set_1)
        assert two_phase_set_1.add_set.payload == {42}
        assert two_phase_set_1.remove_set.payload == {42}
        assert two_phase_set_2.add_set.payload == {42}
        assert two_phase_set_2.remove_set.payload == {42}

    def test_str(self) -> None:
        two_phase_set = TwoPhaseSet()
        assert str(two_phase_set) == "(Add: set(), Remove: set())"

        two_phase_set.add(3)
        assert str(two_phase_set) == "(Add: {3}, Remove: set())"

        two_phase_set.remove(3)
        assert str(two_phase_set) == "(Add: {3}, Remove: {3})"
