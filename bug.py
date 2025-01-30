def function_with_uncommon_error(data):
    try:
        result = 1 / data['value']
        return result
    except KeyError:
        print("Key 'value' not found in the data")
        return None
    except TypeError:
        print("Data must be a dictionary with a 'value' key")
        return None
    except ZeroDivisionError:
        print("The value cannot be zero")
        return None
data = {'value': 0}
result = function_with_uncommon_error(data)
print(result)