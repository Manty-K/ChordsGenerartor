class Scale:
    def __init__(self,name:str,pattern:list):
        self.name = name,
        self.pattern = pattern,

    def info(self):
        print(f"This is {self.name} scale with pattern : {self.pattern}")