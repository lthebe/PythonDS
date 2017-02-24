from lliststack import Stack

def isValidSource(srcfile):
    s = Stack()
    for line in srcfile:
        for token in line:
            if token in "{[(":
                s.push(token)
            elif token in "}])":
                if s.isEmpty():
                    return False
                else:
                    left = s.pop()
                    if (token == "}" and left != "{") or \
                            (token == "]" and left != "[") or \
                            (token == ")" and left != "("):
                        return False
    return s.isEmpty()
