class ArrayListManager:
    '''
     * @param n: You should generate an array list of n elements.
     * @return: The array list your just created.
    '''

    def create(self, n):
        arr = []
        for i in range(n):
            arr.append(i)
        return arr

    '''
     * @param list: The list you need to clone
     * @return: A deep copyed array list from the given list
    '''

    def clone(self, list):
        arr2 = []
        for a in list:
            arr2.append(a)
        return arr2

    '''
     * @param list: The array list to find the kth element
     * @param k: Find the kth element
     * @return: The kth element
    '''

    def get(self, list, k):
        return list[k]

    '''
     * @param list: The array list
     * @param k: Find the kth element, set it to val
     * @param val: Find the kth element, set it to val
    '''

    def set(self, list, k, val):
        list[k] = val

    '''
     * @param list: The array list to remove the kth element
     * @param k: Remove the kth element
    '''

    def remove(self, list, k):
        list.remove(k)

    '''
     * @param list: The array list.
     * @param val: Get the index of the first element that equals to val
     * @return: Return the index of that element
    '''

    def indexOf(self, list, val):
        if list is None:
            return -1
        try:
            ans = list.index(val)
        except ValueError:
            ans = -1
        return ans
