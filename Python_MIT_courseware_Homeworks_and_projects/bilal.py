class student:
    def _init_(self, name, age, task):
        self.name = name
        self.age = age
        self.task = task

    def welcome(self):
        print('Hello', self.name)

    def load(self):
        print('loading....')

    def worklist(self, task):
        tasks = ['reading', 'writing', 'dancing', 'singing']
        return tasks[task]

    def working(self):
        self.load()
        print(self.name, ' is ready to work')
        work = self.worklist(self.task)
        print(self.name, ' is ', work)

obj = student('Ali', 20, 2)
obj.welcome()
obj.load()
obj.working()
