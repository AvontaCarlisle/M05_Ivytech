
# assert sum([1,2,3]) == 6, "should be 6"
# assert sum([5, 1, 8]) == 6, "Should be 6"


def test_sum():
    assert sum([1,2,3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")