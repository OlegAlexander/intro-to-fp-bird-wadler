from intro_to_fp_bird_wadler.ch4.variable_length_arithmetic import (
    strep, align, veq, vadd, vsub, negate, vmul, divalg, vqrm
)


def test_all() -> None:
    assert strep([0, 0, 0, 1, 2, 3]) == [1, 2, 3]
    assert strep([0, 0, 0]) == [0]

    assert align([1, 2, 3], [0, 1, 2, 3]) == ([0, 1, 2, 3], [0, 1, 2, 3])
    assert align([0, 1, 2, 3], [1, 2, 3]) == ([0, 1, 2, 3], [0, 1, 2, 3])
    assert align([1, 2, 3], [1, 2, 3]) == ([1, 2, 3], [1, 2, 3])

    assert veq([1, 2, 3], [1, 2, 3]) == True
    assert veq([0, 1, 2, 3], [1, 2, 3]) == True

    assert vadd([7, 3, 7], [4, 6, 9]) == [1, 2, 0, 6]
    assert vsub([1, 0, 6], [3, 7, 5]) == [-1, 7, 3, 1]
    assert negate([-1, 7, 3, 1]) == [2, 6, 9]

    assert vmul([4, 5, 6], [1, 2, 3]) == [5, 6, 0, 8, 8]

    assert divalg([1, 7, 8, 4], [6, 2]) == [(0, [1]), (0, [1, 7]), (2, [5, 4]), (8, [4, 8])]
    assert vqrm([1, 7, 8, 4], [6, 2]) == ([2, 8], [4, 8])
    assert vqrm([9], [3]) == ([3], [0])
    assert vqrm([1, 2, 3], [4]) == ([3, 0], [3])
