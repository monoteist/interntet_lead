### Техническое задание 

#### Разработайте приложение для бронирования парковочных мест в "офисном центре Фрегат".

Приложение должно иметь две роли сотрудников: "Менеджер", "Сотрудник".

1. Менеджер может добавлять, удалять и редактировать информацию о забронированном времени парковочного места.

2. Сотрудники должны иметь возможность резервировать парковочное место на указанное время.

Список необходимых экранов:
1) Вход в приложение по логину и паролю
2) Список парковочных мест (2 места)
3) Добавление / изменение времени резервирования
4) Добавление / удаление парковочного места

Сдача работы:
1. Необходимо развернуть проект.
2. Отправить ссылку на рабочую версию.
3. Отправить ссылку на репозиторий с проектом.

### Демо

Приложение доступно по ссылке https://internet-lead.herokuapp.com/

### Установка

#### Docker

Перед установкой убедитесь в том что ваша хост машина подерживает виртуализацию, и в том что она включена.

Для Windows: убедитесь в том что у вас включен компонент Hyper-V.

Затем скачайте и установите Docker, Docker-Compose

#### Запуск

Склонируйте репорзиторий к себе!

Для запуска программы используйте:

Команду  `docker compose up --build`

Приложение доступно по адресу http://127.0.0.1:8000/

Войдите под учетной записью `admin` `admin` которая имеет роль MANAGER а также является superuser
