import random

class Queue:
    def __init__(self):  
        self.queue = list()  
    
    def add_element(self,pelicula): 
        self.queue.append(pelicula)

    def display(self):
        print(self.queue)

def shuffle(array):
    random.shuffle(array)
    return array


class Stack:  
  
    def __init__(self):  
        self.stack = list()  
    
    def push_element(self,comida): 
        if comida not in self.stack:  
            self.stack.insert(0,comida)  
            return True  
        return False

    def display(self):
        print(self.stack)

         