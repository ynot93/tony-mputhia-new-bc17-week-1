class BinarySearch(list):
    def _init_(self, a, b):
        self.a = a
        self.b = b

        for i in range(1, a+1):
            self.append(i*b)
        self.a = len(list)

    def search(self, value):
        first_element = self[0]
        last_element = self[-1]
        index_of_value = 0
        index_found = False
        count = 0

        if value == first_element:
            index_of_value = 0
            index_found = True
            return index_of_value

        elif value == last_element:
            index_of_value = -1
            index_found = True
            return index_of_value
        








