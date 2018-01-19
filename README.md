Matryoshka
===============================

author: Vincent Nikolayev

Overview
--------
Unpacks any array with nested-array type-containers into a single level.

Features
--------
* Able to preserve empty containers at their indices
* Able to preserve full strings or unpack them to single length strings ie. 'st' vs. ['s', 't']
* Implements recursion

Requires
-------
* numpy: for the sole reason of passing in its ndarray type

Usage
------------------
```
array = [[[1], 2], ([3], [[4]]), (), 'string']

unpack(array)
out: [1, 2, 3, 4, (), 'string']

unpack(array, preserve_empties=False)
out: [1, 2, 3, 4, 'string']

unpack(array, preserve_empties=False, types=[str])
out: [1, 2, 3, 4, 's', 't', 'r', 'i', 'n', 'g']
```
