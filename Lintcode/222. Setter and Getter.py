class School:
    '''
     * Declare a setter method `setName` which expect a parameter *name*.
    '''

    def __init__(self):
        self.__name = ''

    def setName(self, name):
        self.__name = name

    '''
     * Declare a getter method `getName` which expect no parameter and return
     * the name of this school
    '''

    def getName(self):
        return self.__name
