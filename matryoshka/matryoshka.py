import numpy as np


def unpack(array, preserve_empties=True, types=[]):
    """
    Unpacks any array with nested-array type-containers into a single level array (*note: refer to preserve_empties array for the slight exception to this).

    Example:
        in: [[[1],2],([3],[[4]]), (), 'string']

        out: [1, 2, 3, 4, (), 'string']

        * preserve_empties as False returns [1, 2, 3, 4, 'string']

        *if str is passed into types like [str]. [1, 2, 3, 4, 's', 't', 'r', 'i', 'n', 'g'] is returned

    Params:
        array: input
        preserve_empties (bool): whether to append empty iterable such as [] to returned list
        types (list): allowed iter types. in default string absent.

    Returns:
        unpacked array ex. [1, 2, 'string', 3, 4]
    """

    # select types
    iter_types = [list, tuple, np.ndarray]
    for t in types:
        iter_types.append(t)  # append types to list

    iter_types = tuple(iter_types)  # convert types to tuple

    # recursive function
    def recurse(array):
        for elem in array:
            if isinstance(elem, iter_types):
                if len(elem) == 1 and isinstance(elem, str):  # conditions for str
                    array_unpacked.append(elem)
                elif preserve_empties and len(elem) == 0:  # an empty iterable
                    array_unpacked.append(elem)
                else:  # conditions for iters that are not strings, continue looping
                    recurse(elem)
            else:  # not an iterable
                array_unpacked.append(elem)

    ### MAIN ###
    array_unpacked = []  # holds unpacked elems

    recurse(array)

    return array_unpacked


if __name__ == '__main__':
    array = [[[1], 2], ([3], [[4]]), (), 'string']

    print(unpack(array))
    print(unpack(array, False))
    print(unpack(array, False, types=[str]))
