class example
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
            list1=item.rstrip