# TODO Найдите количество книг, которое можно разместить на дискете
simbols_in_book = 25*50*100
weight_of_book = simbols_in_book * 4
memory_in_bytes = 1.44 * 1024**2
count_of_books = int(memory_in_bytes // weight_of_book)
print("Количество книг, помещающихся на дискету:", count_of_books)
