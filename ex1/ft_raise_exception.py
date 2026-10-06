#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if (temp < 0):
        raise ValueError(temp_str + "°C is too cold for plants (min 0°C)")
    elif (temp > 40):
        raise ValueError(temp_str + "°C is too hot for plants (max 40°C)")
    return (temp)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    try:
        print("\nInput data is '25'")
        temp = input_temperature("25")
        print("Temperature now is ", temp, "°C", sep='')
    except ValueError as e:
        print("Caught input_temperature error:", e)

    try:
        print("\nInput data is 'abc'")
        temp = input_temperature("abc")
        print("Temperature now is ", temp, "°C", sep='')
    except ValueError as e:
        print("Caught input_temperature error:", e)

    try:
        print("\nInput data is '100'")
        temp = input_temperature("100")
        print("Temperature now is ", temp, "°C", sep='')
    except ValueError as e:
        print("Caught input_temperature error:", e)

    try:
        print("\nInput data is '-50'")
        temp = input_temperature("-50")
        print("Temperature now is ", temp, "°C", sep='')
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print("\nAll tests completed - program didn't crash")


if __name__ == "__main__":
    test_temperature()
