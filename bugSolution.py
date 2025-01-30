def function_with_uncommon_error(data):
    try:
        if not isinstance(data, dict):
            raise TypeError("Data must be a dictionary")
        if 'value' not in data:
            raise KeyError("Key 'value' not found in the data")
        value = data['value']
        if value == 0:
            raise ZeroDivisionError("The value cannot be zero")
        result = 1 / value
        return result
    except KeyError as e:
        print(f"KeyError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
        return None
data = {'value': 0}
result = function_with_uncommon_error(data)
print(result) 
