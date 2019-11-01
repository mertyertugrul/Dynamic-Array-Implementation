import ctypes


class DynamicArray(object):
    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.my_array = self.make_array(self.capacity)
        self._index = 0

    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.length

    def __getitem__(self, k):
        """
        Return element at index k
        """
        if not 0 <= k <= self.length:
            # Check it k index is in bounds of array
            return IndexError("K is out of bounds!")
        return self.my_array[k]  # Retrieve from the array at index k

    def __iter__(self):
        """
        Making the calss iterable
        """
        return self

    def __next__(self):
        """
        Next item for iteration
        """
        if self._index < self.length:
            self._index += 1
            return self.my_array[self._index - 1]
        elif self._index == self.length:
            self._index = 0
            # End of Iteration
            raise StopIteration

    def append(self, elm):
        """
        Add element to end of the array
        """
        if self.length == self.capacity:
            # Double capacity if not enough room
            self._resize(2 * self.capacity)

        self.my_array[self.length] = elm  # Set self.n index to element
        self.length += 1

    def pop(self):
        """
        Delete the last item on the array
        """
        last_item = self.my_array[self.length - 1]

        new_array = self.make_array(self.length - 1)

        for k in range(self.length - 1):  # Reference all existing values except last one
            new_array[k] = self.my_array[k]

        self.my_array = new_array
        self.length -= 1
        self.capacity -= 1

        print(str(last_item) + ' has been deleted.')

    def delete(self, index_n):
        """
        Delete any item with given index
        """
        if not 0 <= index_n <= self.length:
            # Check it index is in bounds of array
            return IndexError("Index is out of bounds!")

        deletedItem = self.my_array[index_n]

        new_array = self.make_array(self.length - 1)

        for k in range(self.length):  # Reference all existing values - last one
            if k < index_n:
                new_array[k] = self.my_array[k]
            elif k > index_n:
                new_array[k - 1] = self.my_array[k]

        self.my_array = new_array
        self.length -= 1
        self.capacity -= 1

        print(str(deletedItem) + ' has been deleted.')

    def _resize(self, new_cap):
        """
        Resize internal array to capacity new_cap
        """
        new_array = self.make_array(new_cap)  # New bigger array

        for k in range(self.length):  # Reference all existing values
            new_array[k] = self.my_array[k]

        self.my_array = new_array  # Call A the new bigger array
        self.capacity = new_cap  # Reset the capacity

    @staticmethod
    def make_array(new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()
