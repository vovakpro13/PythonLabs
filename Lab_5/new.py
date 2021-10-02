dictionary = {
    1: [1,2,3],
    "a": ('get', 'set'),
    2: {
        "a": 1,
        "b": 2
    }
}

print(dictionary.get(1)[2], dictionary.get("a")[0], dictionary.get(2).get('a'))