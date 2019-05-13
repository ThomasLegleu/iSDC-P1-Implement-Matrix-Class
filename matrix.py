import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        
        det = 0
        if self.h == 2:
            det = self[0][0]*self[1][1]-self[0][1]*self[1][0]
        else:
            det = self[0][0]
        return det
    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        result = 0
        for i in range(self.h):
            result = result + self[i][i] 
        return result

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        
        inverse = []        
        if self.h == 2:
            det = Matrix.determinant(self)
            #print(det)
            if det == 0:
                raise RuntimeError('The is not invertible')
            else:
                inverse = [[self[1][1]/det, -1*self[0][1]/det],
                          [-1*self[1][0]/det, self[0][0]/det]] 
        else:
            inverse = [[1/self[0][0]]]
        return Matrix(inverse)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        
        matrix_transpose = [[0 for i in range(self.h)] for j in range(self.w)] 
        for i in range(self.h):
            for j in range(self.w):
                matrix_transpose[j][i] = self[i][j]
        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        matrixSum = []
        for i in range(self.h):
            row = [] # create a new list for each row
            for j in range(self.w):
                m_addition = self[i][j] + other[i][j]
                row.append(m_addition)
            matrixSum.append(row)
        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
 
        matrixNeg = []
        
        for i in range(self.h):
            row = [] # create a new list for each row
            for j in range(self.w):
                m_Neg = -1 * (self[i][j])
                row.append(m_Neg)
            matrixNeg.append(row)
        return Matrix(matrixNeg)
   

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        
        #   
        # TODO - your code here
        #
        
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        
        matrixSub = []
        for i in range(self.h):
            row = [] 
            for j in range(self.w):
                m_subtraction = self[i][j] - other[i][j]
                row.append(m_subtraction)
            matrixSub.append(row)
        return Matrix(matrixSub)
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        
        if self.w != other.h :
            raise(ValueError, "Matrices can only be multiplied if the row of one matrix is equal to the column of the other matrix") 
        
        result = 0
        product = []
        for i in range(self.h):
            row_result = []
            for j in range(other.w):
                cell = 0
                for k in range(other.h):
                    cell = cell + self[i][k] * other[k][j]
                row_result.append(cell)          
            product.append(row_result)
        return Matrix(product)
        
        

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            
            r = [] 
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    scalarV = other * self[i][j]
                    row.append(scalarV)
                r.append(row)
            return Matrix(r)
            
            
            
            