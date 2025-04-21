class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None 

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

priority = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

def infix_to_postfix(infix):
    s = Stack()
    postfix = []
    for char in infix.replace(" ", ""):
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            s.push(char)
        elif char == ')':
            while not s.is_empty() and s.peek() != '(':
                postfix.append(s.pop())
            if not s.is_empty():
                s.pop()
        else:
            while (not s.is_empty() and s.peek() in priority and priority[s.peek()] >= priority[char]):
                postfix.append(s.pop())
            s.push(char)
            
    while not s.is_empty():
        postfix.append(s.pop())
    return ' '.join(postfix)

ekspresi_infix = input("Masukkan ekspresi infix: ")
ekspresi_postfix = infix_to_postfix(ekspresi_infix)
print(f"Ekspresi postfix: {ekspresi_postfix}")
