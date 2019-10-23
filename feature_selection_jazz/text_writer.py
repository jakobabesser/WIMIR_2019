import os

class TextWriter:
    def __init__(self):
        self.content = None
        self.reset()

    def reset(self):
        self.content = []

    def add(self, val):
        self.content.append(val)

    def show(self):
        for _ in self.content:
            print(_)

    def save(self, fnTXT):
        with open(fnTXT, 'w+') as f:
            for _ in self.content:
                f.write(_ + '\n')

    
