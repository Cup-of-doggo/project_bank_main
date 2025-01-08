def simple_search(data: list[dict]):
    founded_string = []
    user_input = str(input())
    for data_inf in data:
        for string_to_search in data_inf.values():
            if user_input in str(string_to_search):
                founded_string.append(data_inf)
    return founded_string
