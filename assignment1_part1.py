class ListDivideException(Exception):
    pass

def list_divide(numbers, divide=2):
    try:
        return len([num for num in numbers if num % divide == 0])
    except Exception as e:
        raise ListDivideException(f"An error occurred: {e}")

def test_list_divide():
    try:
        assert list_divide([1, 2, 3, 4, 5]) == 2
        assert list_divide([2, 4, 6, 8, 10]) == 5
        assert list_divide([30, 54, 63, 98, 100], divide=10) == 2
        assert list_divide([]) == 0
        assert list_divide([1, 2, 3, 4, 5], 1) == 5
    except AssertionError:
        raise ListDivideException("One or more test cases failed.")

if __name__ == "__main__":
    test_list_divide()