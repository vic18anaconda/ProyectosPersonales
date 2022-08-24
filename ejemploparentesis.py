def ChechParentesis(string):
    stack = []
    openers = ["(", "[", "{"]
    closers = [")", "]", "}"] 
    for char in string:
        if (char in openers):
            stack.append(char)
        if(char in closers):
            if stack:
                index_closer = closers.index(char)
                c = stack.pop()
                index_opener = openers.index(c)
                if index_closer != index_opener:
                    return False
            else:
                return False
    if stack:
        return False
    else:
        return True

string1 = "([{}])" # true
string2 = "([[{}])" #false
string3 = "([[{}{}]())" #True
string4 = "([[{})()])" #false
string5 = "])([" # true



# print(ChechParentesis(string1))
# print(ChechParentesis(string2))
# print(ChechParentesis(string3))
print(ChechParentesis(string5))