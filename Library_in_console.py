import random


#book1 = {"id":"15254", "title":"да","author":"да","year":"2006","status":"доступна"}

books = []
keys = ['id',"название",'автор','год',"статус"]
id_list = []
free_books = []
bron_books = []

def book_return(x):
      try:
            book_id = int(x)
            book_dict = next((dic for dic in bron_books if dic.get('id') == book_id), None)

            if book_dict:
                  book_dict["статус"] = 'свободно'
                  free_books.append(book_dict)
                  bron_books.remove(book_dict)
                  return "Вы вернули книгу!\n"
            else:
                  return "Книга не занята!\n"
      except ValueError:
            return "Ошибка: Введите корректный id книги (число)\n"

def book_bron(x):
      try:
            book_id = int(x)
            book_dict = next((dic for dic in free_books if dic.get('id') == book_id), None)

            if book_dict:
                  book_dict["статус"] = 'забронированно'
                  bron_books.append(book_dict)
                  free_books.remove(book_dict)
                  return "Вы забронировали книгу. Можете её забрать!\n"
            else:
                  return "Книга занята или не найдена\n"
      except ValueError:
            return "Ошибка: Введите корректный id книги (число)\n"


def find_book_dict(x):
      found_dict = next((dic for dic in books if dic.get('id') == x), None)

      if found_dict:
            book_info = "\n".join([f"{key}: {value}" for key, value in found_dict.items()])
            return book_info + "\n"
      else:
            return "Такой книги не существует\n"

def gen_id():
      while True:
            id = random.randint(10 ** 6, 10 ** 7)
            if len(id_list) == 0 or id not in id_list:
                  id_list.append(id)
                  break
      return id

def book_append(title, author, year):
      for book in books:
            if book['название'] == title and book['автор'] == author and book['год'] == year:
                  return "Такая книга есть в библиотеке"
      id=gen_id()
      status = "свободна"
      new_book = [id,title,author,year,status]
      book_dict = dict(zip(keys, new_book))
      books.append(book_dict)
      free_books.append(book_dict)
      return "Книга добавлена! Её уникальный id: " + str(id)

reg = True
while reg:
      print("1. Добавить книгу""\n2. Показать все книги""\n3. Найти книгу""\n4. Выдать/вернуть книгу""\n5. Загрузить данные"
            "\n6. Выход")
      print("\nВыберите действие (введите число):", end = " ")
      c_menu = str(input())
      if c_menu.isdigit() and 1<=int(c_menu)<=6:
            if c_menu == "1":
                  print("введите название книги:")
                  title = str(input())
                  print("введите автора книги:")
                  author= str(input())
                  print("введите год книги:")
                  year= str(input())
                  if year.isdigit():
                        print(book_append(title, author, year),'\n') # функцию добавления книги и функцию генерации id
                  else:
                        print("Введите число")
                  continue
            elif c_menu == "2":
                  print(books,'\n')
            elif c_menu == "3":
                  print("Найти книгу по:\n1. id \n2. названию \n3. автору \n4. вернуться в меню")
                  c_menu_find = str(input())
                  if c_menu.isdigit() and 1 <= int(c_menu) <= 4:
                        if c_menu_find == "1": # проверку на существование книги
                              print("введите id книги:", end = " ")
                              book_id = str(input())
                              if book_id.isdigit():
                                    print(find_book_dict(int(book_id)))
                              else:
                                    print("Введите число")
                        elif c_menu_find == "2":
                              print("введите название книги:", end = " ")
                              title = str(input())
                              print(find_book_dict(title))
                        elif c_menu_find == "3":
                              print("введите автора книги:", end = " ")
                              author = str(input())
                              print(find_book_dict(author))
                        else: continue;
                  else: print("такого действия не существует\n")
            elif c_menu == "4":
                  print("\n1. Выдать книгу \n2. Вернуть книгу\n3. Вернуться в меню\n\nВыберите действие: ", end='')
                  c_menu_give = input()

                  if c_menu_give.isdigit() and 1 <= int(c_menu_give) <= 3:
                        if c_menu_give == "1":
                              print("Введите id книги:", end=' ')
                              book_id = input()

                              if find_book_dict(book_id):# Проверяем, существует ли книга
                                    if any(dic.get('id') == int(book_id) for dic in free_books): # Проверяем, свободна ли книга
                                          print(book_bron(book_id))
                                    else:
                                          print("Книга уже занята\n")
                              else:
                                    print("Книга не найдена\n")
                        elif c_menu_give == "2":
                              print("Введите id книги:", end=' ')
                              book_id = input()
                              if find_book_dict(book_id):
                                    if any(dic.get('id') == int(book_id) for dic in bron_books):  # Проверяем, свободна ли книга
                                          print(book_return(book_id))
                                    else:
                                          print("Книга не занята!\n")
                        else:
                              continue
                  else:
                        print("Ошибка: Введите число от 1 до 3\n")

            elif c_menu == "5":
                  print("В разработке\n")
            else: continue;
      else: print("\nтакого действия не существует\n")