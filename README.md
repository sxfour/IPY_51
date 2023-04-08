# IPY_51 (индивидуальные приборы учёта)
[ОБНОВЛЕНО 29.03.2023]

Изменения:
- Добавлено логирование некоторых ошибок в стэк
- Автоматическое изменение статусов в таблице при первом входе на тек.дату


[ОБНОВЛЕНО 28.03.2023]

Изменения:
- Фильтр поисковых запросов (Ограничение вкладок).
- Изменено меню редактирование таблицы (Абоненты, поиск)
- Исправлен баг с фильтром поиска.
- Исправлен баг с окном (при входе).
- Добавлена проверка дат при запуске (клиент-сервер)
- Проверка дат сервер-клиент
- Автоизменение дат в таблице

[ОБНОВЛЕНО 26.03.2023]

Изменения:
- Сократил код.
- Добавил поиск по слову.
- Исправлена логика логирования стэка.
- Исправлена логика фильтрации символов и отображения окон.
- Добавлены окна ошибок фильтрации


# Full stack проект, для работы с реляционной базой данных.

![image](https://user-images.githubusercontent.com/112577182/225367670-4f3b8674-92c4-498d-a0da-c1d9459e2b1c.png)

- Основной backend соединения с бд в packages, .ini в postgresql
- Логирование исключений в stack
- UI в main.py, все остальное (окна и тд. по папкам)

На данный момент реализовано:
- Интерфейс (+)
- Соединение с БД (+)
- Аутентификация (-)
- Фильтрация bad requests в строке поиска (+)
- Счётчик просроченых абонентов (+)
- Импортирование абонентов списками в csv (+)
- Соединение с БД более 1 клиента (+)
- Редактирование базы абонентов (+)

# Как редактируется таблица?

При открытии вкладки Абоненты или запроса в поисковую строку, создается запрос к базе с указанием ключевого слова или всех абонентов.
Отображение в режиме просмотра и редактирования.
![image](https://user-images.githubusercontent.com/112577182/230734926-b5335b59-2cf4-4497-a3cf-6094f0c24070.png)

# Как происходит фильтрация запроса пользователя в интерфейсе?

Для защиты от потери данных в базе или случайном редактировании, создан фильтр в котором полностью исключены англ буквы. 
Каждый запрос проверяется и раскладывается на список, если есть совпадение с запрещённым символом - фильтруется.

![image](https://user-images.githubusercontent.com/112577182/230734572-88fc62cb-184f-4866-8486-a26d9f00ab3d.png)

В основном для поиска, пользователь будет использовать кириллицу.

![image](https://user-images.githubusercontent.com/112577182/230734764-b8b43b41-0534-4a97-83cc-b0214e571db7.png)

Ниже приведён пример функции фильтрации запроса пользователя.

![image](https://user-images.githubusercontent.com/112577182/230734645-40c5d608-587f-4cea-95d0-eb9ae13a8c39.png)

# Как происходит синхронизация дат времени клиент-сервер?
Создана функция которая проверяет при запуске время клиента и сервера.

![image](https://user-images.githubusercontent.com/112577182/230734425-cac69818-f4c1-4158-a44d-a916a6e6371e.png)

Если оба параметра совпадают, то происходит синхронизация с базой данных.

![image](https://user-images.githubusercontent.com/112577182/230734344-f30db470-ccc8-4019-bf93-e08f95c61b99.png)


# Соединение с помощью PostgreSQL.

![image](https://user-images.githubusercontent.com/112577182/230734023-d70e0ee4-c4b1-4f67-a975-0b653f9b64ee.png)

Таблица создана через импорт csv файла в postgreSQL
c помощью команды \COPY tickets FROM ‘Локальный csv’ DELIMITER ‘,’ CSV HEADER;

![image](https://user-images.githubusercontent.com/112577182/230734130-592dd931-fc74-4ddc-ba42-88ce245ea321.png)

Где tickets – название созданной в БД таблицы, из – путь, где хранится  .csv-файл, DELIMITER ‘,’ – разделитель, используемый в импортируемом .csv-файле, сам формат файла и HEADER, указывающий на заголовки «колонок».
