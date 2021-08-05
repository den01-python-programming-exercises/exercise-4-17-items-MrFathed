from item import Item

def main():
    #write your code below this line
    items = []

    while True:
        name = input()

        if not name:
            break

        items.append(Item(name))

    for item in items:
        print(item)

if __name__ == '__main__':
    main()
