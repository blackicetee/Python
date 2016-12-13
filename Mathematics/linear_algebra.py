############### Matrices ###############

# Imports matrix from library NumPy
from numpy import matrix, mat
# Shape from NumPy is a funciton to print out the dimensions of a matrics
from numpy import shape

# ss is a matrix of coefficients
ss = matrix([[2, -1], [-1, 2]])

# mm is a matrix of unknown
mm = mat([['x'], ['y']])

# Redefining mm with literals
mm = mat([[0], [3]])

# kk is a matrix with a column consist of 0's
kk = mat([1, 0, 2])

# Functions for scalar operations, a scalar operation is when a matrix is multiplyed or added by a number
def scalar_multiplication(matrix, scalar_factor):
	return matrix * scalar_factor

def scalar_addition(matrix, scalar_summand):
	return matrix + scalar_summand

# CAUTION!!! You can multiply matrices like (1x3) * (3x1) or (2x3) * (3x1)
# But you can't multiply matrices like (1x3) * (1x3)
# If the matrices have inner matching dimensions [] like (2x4)(4x1) inner dimension = (2x"4")("4"x1)
# The dimension of the result matrix is what you get when you drop the inner dimensions ("2"x4) * (4x"1") = (2x1) 
def matrix_multiplication(first_matrics, second_matrics):
	return first_matrics * second_matrics

# Checks if a matrix is square
def is_matrix_square_version_1(matrix):
	return True if shape(matrix)[0] == shape(matrix)[1] else False

# Checks if a matrix is square
def is_matrix_square_version_2(matrix):
	return len(matrix) == len(matrix.T)

# Check if a matrix is full range (has no column with only zeros)
def is_matrix_full_range(matrix):
	for col in matrix.T:
		if col.mean() == 0:
			return False
	return True
				
print 'ss = ' + str(ss)
print 'mm = ' + str(mm)

print 'Scalar multiplication: ss * mm[1, 0] = ' + str(scalar_multiplication(ss, mm[1, 0]))
print 'Scalar additions: ss * mm[1, 0] = ' + str(scalar_addition(ss, mm[1, 0]))
print 'matrix multiplication: ss * mm = ' + str(matrix_multiplication(ss, mm))

print 'Shape of matrix ss = ' + str(shape(ss))
print 'Is matrix ss square version 1? ' + str(is_matrix_square_version_1(ss))
print 'Is matrix ss square version 2? ' + str(is_matrix_square_version_2(ss))
print 'Is matrix kk full range? ' + str(is_matrix_full_range(kk))
print 'Is matrix ss full range? ' + str(is_matrix_full_range(ss))

############### Vi(m) commands! ###############
# ":set number" prints the row numbers inside of the vim editor
# ":set nonumber" turns of the row numbers
#
# press CTRL + N for a list of auto complete words

############### File "~/.vimrc" ###############
# if you want to change the default settings of the vi(m) editor then change the file ~/.vimrc
# just tipe into the concole "sudo vim ~/-vimrc" but without the ""
# then enter commands like "set number" without ":" a colon sign
# you just need the colon sign when you want to change the settings temporarly
