n = int(input())
book_list = {}

for i in range(n):
    book = input()
    if book not in book_list:
        book_list[book] = 1
    else:
        book_list[book] += 1

freq = max(book_list.values())

best_seller=[]

for book, value in book_list.items():
    if value == freq:
        best_seller.append(book)

best_seller.sort()
print(best_seller[0])