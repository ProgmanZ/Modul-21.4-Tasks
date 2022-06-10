# Задача 3. Помощь другу

def create_dict(input_data, template=None):
    if template is None:
        template = dict()
    if isinstance(input_data, dict):
        return input_data
    if isinstance(input_data, int) or isinstance(input_data, float) or isinstance(input_data, str):
        template[input_data] = input_data
        return template


def data_preparation(old_list):
    new_list = [create_dict(i_element) for i_element in old_list if create_dict(i_element)]
    return new_list


data = ["sad", {"sds": 23}, {43}, [12, 42, 1], 2323]

data = data_preparation(data)

print(data)
