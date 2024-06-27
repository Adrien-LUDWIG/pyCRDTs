from pycrdts import run


def test_run():
    assert run(["a", "bc", "abc"]) == "abc"
