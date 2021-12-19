from iter_class import NestedListIterable
from generator import flat_generator


if __name__ == '__main__':

    nested_list_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    nested_list_2 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]

    print('----Task number 1---')

    for item in NestedListIterable(nested_list_1):
        print(item)

    print('--------------------')

    flat_list = [item for item in NestedListIterable(nested_list_1)]
    print(flat_list)

    print('----Task number 2---')

    for item in flat_generator(nested_list_2):
    	print(item)