import pickle

class Node:
    def __init__(self, value,
                 prev_pointer=None, next_pointer=None):
        self.set_value(value)
        self.set_prev(prev_pointer)
        self.set_next(next_pointer)

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next_pointer

    def get_prev(self):
        return self._prev_pointer

    def set_value(self, value):
        self._value = value

    def set_prev(self, prev_pointer):
        self._prev_pointer = prev_pointer

    def set_next(self, next_pointer):
        self._next_pointer = next_pointer

    def __str__(self):
        return str(self.get_value())

class List:
    def __init__(self, collection = None):
        self._start_pointer = None
        self._finish_pointer = None
        self._length = 0

    def __len__(self):
        return self._length

    def append(self, value):
        if self._length == 0:
            self._start_pointer = Node(value)
            self._finish_pointer = self._start_pointer
            self._length = 1
        else:
            self._finish_pointer.set_next(Node(value,
                                               self._finish_pointer))
            self._finish_pointer = self._finish_pointer.get_next()
            self._length += 1

    def __getitem__(self, i):
        if i < 0 or i >= self._length:
            return False

        curr_pointer = self._start_pointer
        for j in range(i):
            curr_pointer = curr_pointer.get_next()
        return curr_pointer.get_value()

    def __str__(self):
        arr = []
        for i in range(self._length):
            arr.append(str(self[i]))
        return "[" + ", ".join(arr) + "]"

    # сам итератор
    def __iter__(self):
        return StackIterator(self)

    # тут запись в бинарник:
    def save_bin(self, name):
        with open(name, mode="wb") as f: # записываем в двоичном режиме
            pickle.dump(self, f)
    
    @staticmethod # декоратор нужен, так как иначе не сможем без экземпляра класса открыть файл с информацией об экземпляре класса
    def read_bin(name):
        while True:
            try:
                with open(name, mode="rb") as f:
                    l = pickle.load(f)
                    break
            except FileNotFoundError:
                print('Нет файла с таким названием, введите его еще раз:')
                name = input()
        return l

# взял из конспекта семинаров(файл был iter.py)
class StackIterator:
    def __init__(self, stack):
        self._stack = stack
        self._index = len(stack) #индекс элемета к которому обращаемся

    # итератор должен уметь менять свое состояние(чтобы переходить к следующему элементу)

    def __next__(self):
        self._index -= 1 # идем с конца стека, first in, first out
        res = self._stack[self._index]
        if self._index < 0:
            raise StopIteration
        
        return res


A = List()
for i in range(5):
    A.append(i)

for i in A:
    print(i)

A.save_bin('test.bin')
B = List.read_bin('test.bin')
print(B)





