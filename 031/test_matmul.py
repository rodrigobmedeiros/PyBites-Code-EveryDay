from matmul import Matrix


class MatrixWithoutMatMul(object):

    def __init__(self, values):
        self.values = values
        self.col = len(values[0])
        self.row = len(values)

    def __matmul__(self, other):
        return NotImplemented


def test_matmul():
    mat1 = Matrix([[1, 2], [3, 4]])
    mat2 = Matrix([[11, 12], [13, 14]])
    mat3 = mat1 @ mat2
    assert mat3.values == [[37, 40], [85, 92]]
    mat3 = mat2 @ mat1
    assert mat3.values == [[47, 70], [55, 82]]


def test_rmatmul():
    mat1 = Matrix([[1, 2], [3, 4]])
    mat2 = MatrixWithoutMatMul([[11, 12], [13, 14]])
    # mat2 does not implement matmul, so mat1's rmatmul is called
    # which results in mat1 @ mat2
    ret = mat2 @ mat1
    assert ret.values == [[37, 40], [85, 92]]


def test_imatmul():
    mat1 = Matrix([[11, 12], [13, 14]])
    org_id_of_mat1 = id(mat1)
    mat2 = Matrix([[1, 2], [3, 4]])
    mat1 @= mat2
    id_of_mat1_after_inplace_operation = id(mat1)
    assert mat1.values == [[47, 70], [55, 82]]
    # as @= is in place, the id of the object should not change!
    assert org_id_of_mat1 == id_of_mat1_after_inplace_operation


def test_imatmul_other_way_around():
    mat1 = Matrix([[11, 12], [13, 14]])
    mat2 = Matrix([[1, 2], [3, 4]])
    org_id_of_mat2 = id(mat2)
    mat2 @= mat1
    id_of_mat2_after_inplace_operation = id(mat2)
    assert mat2.values == [[37, 40], [85, 92]]
    assert org_id_of_mat2 == id_of_mat2_after_inplace_operation