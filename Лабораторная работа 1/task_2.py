volume_floppy_disk_mb = 1.44  # объём дискеты в Мб
pages = 100  # количество страниц в книге
lines = 50  # число строк на странице
symbols = 25  # количество символов в строке
volume_symbol = 4  # объём символа в байтах

volume_floppy_disk_b = volume_floppy_disk_mb * (1024 ** 2)
volume_book = symbols * lines * pages * volume_symbol
quantity_of_books = volume_floppy_disk_b / volume_book

print("Количество книг, помещающихся на дискету:", int(quantity_of_books))
