# IPY_51 (индивидуальные приборы учёта)

# Full stack проект для работы с реляционной базой данных.
Пример работы:

https://user-images.githubusercontent.com/112577182/233447091-60ba8f29-7d7b-4cb6-9e66-ea31b8e67ab5.mp4

- Основной backend соединения с бд в packages, .ini в postgresql
- Логирование исключений.
- UI в main.py, все остальное (окна и тд. по папкам)

На данный момент реализовано:
- Интерфейс (+)
- Соединение с БД (+)
- Аутентификация пользователя с записью mac в PostgreSQL (+)
- Фильтрация bad requests в строке поиска (+)
- Счётчик просроченых абонентов (+)
- Импортирование абонентов списками в csv (+)
- Соединение с БД более 1 клиента (+)
- Редактирование базы абонентов (+)

# Compitable Windows 10 (64bit,32bit)

# Авторизация пользователя.

![изображение](https://github.com/sxfour/IPY_51/assets/112577182/cbb77145-fdc8-435b-b727-ecd24ce174ac)

Для каждого имени создается UUID с содержанием строки Имени и мак адреса устройства,поэтому
при входе в приложение, в базе пользователей должны совпадать эти параметры с имеющимся мак адресом.


# Отправка обращений через SMTP.
Для связи с администратором создана вкладка создать тикет.

![image](https://user-images.githubusercontent.com/112577182/230735335-ca86148a-b506-4b8e-8a48-e5b5da9fd9d2.png)

Отправка детальной информации о клиенте в письме.

![изображение](https://github.com/sxfour/IPY_51/assets/112577182/b3254ace-9ae4-4be0-a18b-3c858e6da5dc)

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
Создана функция, которая проверяет при запуске время клиента и сервера.

![image](https://user-images.githubusercontent.com/112577182/230734425-cac69818-f4c1-4158-a44d-a916a6e6371e.png)

Если оба параметра совпадают, то происходит синхронизация с базой данных.

![image](https://user-images.githubusercontent.com/112577182/230734344-f30db470-ccc8-4019-bf93-e08f95c61b99.png)


# Соединение с помощью PostgreSQL.

![image](https://user-images.githubusercontent.com/112577182/230734023-d70e0ee4-c4b1-4f67-a975-0b653f9b64ee.png)

Таблица создана через импорт csv файла в postgreSQL
c помощью команды \COPY tickets FROM ‘Локальный csv’ DELIMITER ‘,’ CSV HEADER;

Для сортировки и удобного редактирования, и поиска по таблице создан автоинкремент (id)

![image](https://user-images.githubusercontent.com/112577182/230734130-592dd931-fc74-4ddc-ba42-88ce245ea321.png)

Где tickets – название созданной в БД таблицы, из – путь, где хранится  .csv-файл, DELIMITER ‘,’ – разделитель, используемый в импортируемом .csv-файле, сам формат файла и HEADER, указывающий на заголовки «колонок».

# Логирование.
![image](https://user-images.githubusercontent.com/112577182/230735446-c98dcdf4-995f-4828-8fa3-feb2b79f962b.png)

![изображение](https://user-images.githubusercontent.com/112577182/233073098-e551148a-c2d1-4b0d-afdd-d67d028ff411.png)

# Все изменения
 [11.03.2024] Изменения:
 - Автовход на странице авторизации (сохранение данных в json)
 - Управление в окнах с помощью hotkey (ENTER)
   
 [26.05.2023] Изменения:
 - Оптимизация кода.

 [10.05.2023] Изменения:
 - UUID имён авторизации на основе mac устройства и имени устройства.
 - Авторизация / регистрация через данные сервера с проверкой mac устройства.
 - Добавлен фильтр в окно авторизации / регистрации.
 
 [20.04.2023] Изменения:
 - Добавлена страница авторизации.
 - Добавлена детальная информация в письме о клиенте, при отправке через SMTP.

 [09.04.2023] Изменения:
 - Исправлен баг с отображением лишних данных в списке.
 
 [06.04.2023] Изменения:
 - Добавлено полное редактирование таблицы (ключевой и полной).
 - Обновлён интерфейс вкладки Абоненты.
 - Добавлена вкладка для создания новых пользователей в таблицу.
 - Исправлен баг с ошибкой при редактировании таблицы.
