class example:
    names=[]
    heights=[]
    tsh=[]
    tsc=[]

    def __init__(self):
        pass

    def readData(self):
        file=open('example.txt', mode='r', encoding='utf-8')
        data=file.readlines()
        print('data: ',data)

        for item in data:
            list1 = item.rstrip('\n')  # 'Sam,18\n'-> remove \n
            list2 = list1.split(',')  # Split 'Sam, 18'
            # print(list2)#['Sam','18']
            # print(list2[0]#'Sam'
            # print(list2[1]#18
            self.names.append(list2[0])  # store Sam in nameList
            self.heights.append(float(list2[1]))  # convert and store 18 in ageList
            file.close()

            # outside for loop
        print('names:', self.names)
        print('heights:', self.heights)

        # Store a new name into ageList
        userinput = input('Enter a new name: ')

        self.names.append(str(userinput))
        print('Updated names:', self.names)

        userinput = input("Enter a new height: ")
        while userinput.isnumeric() == True:  # check user input is a number
            userinput = input('Enter a new height:')

        # height to userinput
        self.heights.append(float(userinput))
        print('Updated heights:', self.heights)

        # Number of heights in ageList
        self.numberofHeights = len(self.heights)

        # Create function to calculate average height

    def example(self):
        totalHeights = 0
        # loop through height and add each item to total heights
        for item in self.heights:
            totalHeights = totalHeights + item  # convert to int
        # return average age

        return totalHeights / self.numberofHeights


classInstance=
classInstance.readData()
print('Student average height is:', round(classInstance.example(), 2), 'm for', classInstance.numberofHeights,
          'students.')

