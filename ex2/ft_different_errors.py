#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
        2 / 0
    elif (operation_number == 2):
        open('/file.txt')
    elif (operation_number == 3):
        print("Hello " + 123)
    else:
        return


def test_error_types(op_num: int) -> None:
    try:
        print("Testing operation ", op_num, "...", sep='')
        garden_operations(op_num)
        print("Operation completed succesfully")
    except ValueError as error:
        print("Caught ValueError:", error)
    except ZeroDivisionError as error:
        print("Caught ZeroDivisionError:", error)
    except FileNotFoundError as error:
        print("Caught FileNotFoundError:", error)
    except TypeError as error:
        print("Caught TypeError:", error)


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types(0)
    test_error_types(1)
    test_error_types(2)
    test_error_types(3)
    test_error_types(4)
    print("\nAll error types tested succesfully!")
