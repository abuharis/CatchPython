class Reverse(list):
    def __reversed__(self):
        return self[::-1]

bs = Reverse([1, 4,5,6 ,7])

cb = Reverse()
cb.reverse()
print("Original" )
print(bs)

print("Reversed")
print(reversed(bs))

print(reversed([12, 234,4 ]))
