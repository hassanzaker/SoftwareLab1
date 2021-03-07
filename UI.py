from Core import process
def get_input():
    print('->', end=" ")
    return input()

def show_output(text):
    print("===>", end=" ")
    print(text)


text = get_input()
while text != 'end':
    ans = process(text)
    show_output(ans)
    text = get_input()