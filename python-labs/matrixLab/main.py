class Matrix:
    '''
    data is a list. order is a tuple of (rows, columns)
    Maybe explore some arg checking?
    '''

    # Constructor
    def __init__(self, data, order):
        # Check if 'order' is a tuple of two integers
        if not isinstance(order, tuple) or len(order) != 2 or not all(isinstance(i, int) for i in order):
            raise ValueError(
                "Invalid 'order' argument. It should be a tuple of two integers (rows, columns).")

        self._rows, self._columns = order  # Store the number of rows and columns

        # Check if order argument matches data dimensions. If not, raise an exception
        if len(data) != self._rows * self._columns:
            raise ValueError(
                "Mismatch between 'data' dimensions and 'order' dimensions.")

        # Check if ALL entries are numeric. If not, raise an exception
        if not all(isinstance(num, (int, float)) for num in data):
            raise ValueError("All entries in 'data' must be numeric.")

        self._data = data  # Load the matrix by copying data argument into instance variable

    # Dunder method to overload the string representation
    def __str__(self):
        # Initialize an empty string and concatenate data and row delimiters
        result = ""

        # Loop through rows
        for i in range(self._rows):
            result += "| "

            # Loop through columns within the current row
            for j in range(self._columns):
                # Calculate the index in the data list using row and column indices
                index = i * self._columns + j
                result += str(self._data[index]) + " "

            result += "|\n"  # Add the row delimiter

        return result

    # Dunder method to overload addition operator '+'
    def __add__(self, other):
        # Check if rows and columns of both matrices match
        if self._rows != other._rows or self._columns != other._columns:
            raise ValueError("Matrix dimensions must match for addition.")

        # Create an empty list to store the sum
        result_data = []

        # Loop through rows and columns
        for i in range(self._rows):
            for j in range(self._columns):
                # Calculate the index in the data list using row and column indices
                index = i * self._columns + j
                # Add corresponding elements from both matrices
                sum_element = self._data[index] + other._data[index]
                result_data.append(sum_element)

        # Create a new Matrix object with the sum data and the same order
        result_matrix = Matrix(result_data, (self._rows, self._columns))

        return result_matrix


if __name__ == "__main__":
    mat = Matrix([1, 2, 3, 4, 5, 6], (3, 2))
    mat2 = Matrix([11, 12, 13, 14, 15, 16], (3, 2))

    print("Matrix 'mat':")
    print(mat)

    print("Matrix 'mat2':")
    print(mat2)

    # Add them, print the result
    sum_mats = mat + mat2

    print("Sum of the above matrices:")
    print(sum_mats)
