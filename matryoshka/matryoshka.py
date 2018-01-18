import numpy as np


def unpack_arrays(array, preserve_empties=True, types=[]):
    """
    Unpacks any array with nested-array type-containers into a single level array (*note: refer to preserve_empties array for the slight exception). DOES NOT unpack strings (ie. 'st' ==> 's','t') - refer to unpack_all_iters for such functionality. If the str type is passed into types, then an endless loop is created. This is because a string of 1 element is endlessly iterated over. unpack_arrays has more real-world use-cases than the unpack_all_iters.

    Example:
        in: [[[1],2], 'string',([3],[[4]]), ()]

        out: [1, 2, 'string', 3, 4, ()]

        * preserve_empties as False returns [1, 2, 'string', 3, 4]

    Params:
        array: input ie. [[[1],2], 'string',([3],[[4]]), ()]
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

    ###### MAIN ######
    while True:
        array_unpacked = []
        iter_test = False
        test_elems = []

        for elem in array:
            if isinstance(elem, iter_types):
                try:
                    elem[0]  # catches exception
                    array_unpacked.extend(elem)  # extend list with elements within
                    iter_test = True
                except Exception:  # no zero element in iterable
                    if preserve_empties:
                        array_unpacked.append(elem)
                    iter_test = False

            else:  # not an iterable
                array_unpacked.append(elem)
                iter_test = False

            test_elems.append(iter_test)

        array = array_unpacked.copy()  # rewrite main array

        if not any(test_elems):  # if no iterables left
            break

    return array_unpacked


def unpack_all_iters(array):
    """
    Unpacks any array with sub-iterables into a single array. unpacks strings unlike unpack_arrays function.

    Example:
    in: [[[1],2], 'string',([3],[[4]]), ()]

    out: [1, 2, 's', 't', 'r', 'i', 'n', 'g', 3, 4]

    Params:
        array: input

    Returns:
        unpacked array
    """
    while True:
        array_unpacked = []
        iter_test = False
        for elem in array:
            try:
                iter(array)  # catches exception
                array_unpacked.extend(elem)
                iter_test = True
            except TypeError:
                array_unpacked.append(elem)
                iter_test = False

        array = array_unpacked.copy()

        if not iter_test:
            break

    return array_unpacked


if __name__ == '__main__':
    array = [[[1], 2], 'string', ([3], [[4]]), ()]

    print(unpack_arrays(array))
    print(unpack_arrays(array, False))
    print(unpack_all_iters(array))
