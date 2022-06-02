class student:
    def __init__(self, name, age, task):
        self.name = name
        self.age = age
        self.task = task

    def welcome(self):
        print('Hello', self.name)

    def load(self):
        print('loading .....')
    
    def worklist(self, task):
        task = ['reading', 'writing', 'dancing', 'singing']
        # will return the element of task according to self.task
        return task[self.task]
    
    def working(self):
        
        self.load()
        print(self.name, 'is ready to work')
        # worklist will take argument self.task instead of task
        self.work = self.worklist(self.task)
        # har class ke method or variable ke sath self. zaroor aye ga
        print(self.name, 'is', self.work)

obj = student('ali', 23, 1)
obj.welcome()
obj.working()

obj1 = student('Bilal', 23, 3)
obj1.welcome()
obj1.working()





    