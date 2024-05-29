data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum_0(*data_structure):
    s = []

    if (isinstance(*data_structure, list) or isinstance(*data_structure, tuple)
            or isinstance(*data_structure, set)):
        return sum(map(calculate_structure_sum_0, *data_structure), s)
    else:
        return [*data_structure]


def calculate_structure_sum_1(*data_structure):
    s = []

    if (isinstance(*data_structure, list) or isinstance(*data_structure, tuple)
            or isinstance(*data_structure, set)
            or isinstance(*data_structure, dict)):
        return sum(map(calculate_structure_sum_1, *data_structure), s)
    else:
        return [*data_structure]


def sum_(params):
    num = 0
    num_1 = 0
    for i in range(len(params)):
        if type(params[i]) == type(1):
            num = num + params[i]
        else:
            num_1 = num_1 + len(params[i])
    return num + num_1


def dict_sum(my_dict1):
    dicts_ = []
    for i in range(len(my_dict1)):
        if isinstance(my_dict1[i], dict):
            dicts_.append(my_dict1[i])
    un_dict_over = []
    for i in range(len(dicts_)):
        un_dict_over.append(sum(dicts_[i].values()))
    a = sum(un_dict_over)
    return a


def calculate_structure_sum(data_structure):
    result1 = calculate_structure_sum_1(data_structure)
    result2 = (sum_(result1))
    result3 = calculate_structure_sum_0(data_structure)
    result = dict_sum(result3)
    print(result2 + result)


calculate_structure_sum(data_structure)
