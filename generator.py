
def flatten_list(collection: list):
    res_list = []
    for item in collection:
        res_list.extend(flatten_list(item) if isinstance(item, (list, tuple, set)) else [item])
    return res_list


def flat_generator(collection: list):
    flat_list = flatten_list(collection)
    for item in flat_list:
        yield item