from chord_type import ChordType

class PChord:
    def __init__(self,index:int,type:ChordType):
        self.index = index - 1
        self.type = type
