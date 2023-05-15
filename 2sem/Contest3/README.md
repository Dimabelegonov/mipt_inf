# Description
1. Install ```pytest```. To do this run the command in the terminal: 
```bash
pip3 install pytest
```
2. Complete the code in tasks.py file. Write the code where ```# TODO``` comment is placed.

3. Run the tests to check that your code is working properly.
```python
pytest tests.py
```
4. Upload your homework in gitlab repository and send the link in telegram.

# Task 1
Вам даны три списка (list) студентов:
- learners_french - изучающие французский язык
- pianists - владеющие игрой на фортепиано
- swimmers - занимающиеся плаванием

Создайте программу, вычисляющую список пловцов-пианистов, не изучающих французский.


# Task 2
Вам даны два списка чисел list_1 и list_2. 
1) Подсчитайте количество уникальных в первом списке реализовав метод get_unique_list_1
2) Подсчитайте количество уникальных среди обоих списков реализовав метод get_unique_both_lists 


# Task 3
У каждого первокрусника спросили: "Какой ваш любимый фильм?". Ответы записали. 
Необходимо вывести рейтинг фильмов с количеством голосов за каждый в порядке убывания.
Необходимо реализовать метод get_results, который возвращает dict.


# Task 4
Вам дан текст (str). 
Напишите программу, подсчитывающую количество каждого слова в тексте. В тексте присутствует пунктуация. Слова с заглавной и строчной буквы не различать. Итоговый список слов и их количества в тексте выводить в порядке убывания по количеству.


# Task 5
Вам дан словарь d, в котором ключ - имя человека, а значение - список родителей. Напишите функции, которые по имени человека name сообщают о его родственниках.

Вот список методов для реализации:

- parents(name) - возвращает список родителей
- grandparents(name) - возвращает список бабушек и дедушек
- sibling(name) - возвращает список родных братьев и сестёр
- children(name) - возвращает список детей
- grandchildren(name) - возвращает список внуков и внучек
