from generator import flatten_list


class NestedListIterable():

    def __init__(self, collection: list):
        self._collection = flatten_list(collection)

    def __iter__(self):
        return iter(self._collection)