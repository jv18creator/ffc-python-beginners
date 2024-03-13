name = 'Jeet'
count = 1
def greeting(name):
    print(name)

greeting('Viramgama')

def another():
    color = 'Pink'
    global count 
    count += 4
    def greeting(name):
        nonlocal color
        print(color)
        color = 'Red'
        print(name)

    greeting('Viramgama')
    print(color)


another()
print(count)