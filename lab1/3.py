# TODO Найдите количество книг, которое можно разместить на дискете
megabytes_to_kilobytes = 1024
kilobytes_to_bytes = 1024
disc_capacity = 1.44 * megabytes_to_kilobytes * kilobytes_to_bytes
pages_per_book = 100
lines_per_page = 50
symbols_per_line = 25
bytes_for_symbol = 4
book_size = pages_per_book * lines_per_page * symbols_per_line * bytes_for_symbol

print("Количество книг, помещающихся на дискету:", int(disc_capacity // book_size))
