"""
Implement an interpreter like post-fix calculator. Your program should repeatedly:
-Print a prompt to the user. The promt should be: '-->'
-Read an expression from the user
-Evaluate that expression
-Print the result
"""
#Not finished only partially works
def calculate(string):
    string_list = string.split()
    new_string = ''.join(string_list)
    stack = []
    for elem in new_string:
        if elem.isdigit():
            stack.append(int(elem))

    if len(stack)>1:    
        first = stack.pop()
        second = stack.pop()

    if elem == '+':
        stack.append(second + first)
    elif elem == '-':
        stack.append(second - first)
    elif elem == '*':
        stack.append(second * first)
    elif elem == '/':
        stack.append(second / first)

    return stack.pop()
    
def main():
    string = input("-->")
    while string != "done":
        print(calculate(string))
        string = input("-->")
main()
