def find_by_value(obj, value):
    results = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if v == value:
                results.append(obj)
            results.extend(find_by_value(v, value))
    elif isinstance(obj, list):
        for item in obj:
            results.extend(find_by_value(item, value))
    return results

print(find_by_value(data, "john@example.com"))