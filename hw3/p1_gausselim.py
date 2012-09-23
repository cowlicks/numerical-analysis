import numpy

# Create the Matrix.
A = numpy.array(   [[1., 1., 1., 1., 1.,],
                    [1., 1., 2., 3., 2.,],
                    [-1., 0., 2., 1., 1.,],
                    [3., 2., -1., 0., 1.,]])

# Zero an element in a row by adding the pivot row.
def zero_row(A, piv_indx, zero_row_indx):
    m = - float(A[zero_row_indx, piv_indx]) / A[piv_indx, piv_indx]
    A[[zero_row_indx]] += m * A[[piv_indx]]

# First get the matrix in upper triangular form.
for piv_indx in range(len(A)):
    # Get the pivot.
    pivot = A[piv_indx, piv_indx]

    # Check if pivot is nonzero. If it is swap rows with one whos pivot 
    # would be nonzero.
    while pivot == 0:
        # Get list of elements below the pivot in the same column.
        new_pivots = [ A[j, piv_indx] for j in range(piv_indx, len(A)) ]
        # Choose the row with the largest element.
        indx = piv_indx + new_pivots.index(max(new_pivots))
        # Swap the rows.
        A[[piv_indx, indx]] = A[[indx, piv_indx]]
        # Get pivot again
        pivot = A[piv_indx, piv_indx]

    # Make elements below the pivot zero.
    for zero_indx in range(piv_indx + 1, len(A)):
        zero_row(A, piv_indx, zero_indx)

count = []
# Now do gaussian elimination.
for row in reversed(range(len(A))):
    for i in count:
        A[row, len(A)] += -A[row, i]*A[i, len(A)]
        A[row, i] = 0
    A[[row]] = A[[row]] / A[row, row]
    count.append(row)
print A
