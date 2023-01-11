# API социальной сети "Yatube"

### **Описание проекта**
В проекте реализован интерфейс API, благодаря которому социальная сеть "Yatube" сможет взаимодействовать с другой программой.


### **Запускаем проект в dev режиме на OC Linux**
Клонировать репозиторий с GitHub
```
git clone git@github.com:madina-zvezda/api-Yatube.git
```

Установить виртуальное окружение venv
```
python3 -m venv venv
```

Aктивировать виртуальное окружение venv
```
source venv/bin/activate
```

Обновить менеджер пакетов pip
```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

Выполнить миграции
```
python3 manage.py migrate
```

Создать суперпользователя
```
python3 manage.py createsuperuser
```

Запустить проект
```
python3 manage.py runserver
```


