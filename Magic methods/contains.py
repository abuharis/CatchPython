class Items:
    def __init__(self, items):
        self.items = items


    def __contains__(self, item):
        print("Searching an item")
        print(f'"{item}" in {self.items}')

        return item in self.items
if __name__ == '__main__':
    my_items = Items([1, 23, 'b'])
    print('b' in my_items)


