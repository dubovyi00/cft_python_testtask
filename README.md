## О приложении
Данный веб-сервис позволит вам подсчитать количество пикселей заданного цвета на загруженной вами картинке.
Имеет два режима:
* "Чёрные vs белые" - подсчёт количества чёрных и белых пикселей, а также вывод, какого цвета будет больше
* "Цвет по HEX-коду" - подсчёт количества пикселей по заданному пользователем цвету

## Запуск
1. Активируйте виртуальное окружение Python командой source venv/bin/activate. Это и дальнейшие действия необходимо выполнять на любом дистрибутиве Linux.
2. Установите необходимые для работы приложения библиотеки. Для запуска необходимы Django, Django REST Framework, Pillow, Numpy и requests. Делается это командой pip3 install django djangorestframework pillow numpy requests.
3. Запустите сервер. Команда: cd cft_testframework && python3 manage.py runserver 
4. Приложение будет доступно по адресу 127.0.0.1:8000

## Ограничения
* Обработка изображений размером больше 7000*7000 пикселей осуществляться не будет
* Количество поддерживаемых форматов ограничено лишь возможностями библиотеки Pillow. Всего их больше 20 (включая наиболее используемые PNG, GIF и JPG), подробнее можно узнать здесь: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
* Режим "Чёрные vs. белые" умеет работать с цветовыми схемами:
** RGB/RGBA
** CMYK
** Lab
** 8-битная палитра GIF
** чёрно-белые цветовые схемы
* Режим "Цвет по HEX-коду" умеет работать с цветовыми схемами:
** RGB/RGBA
** 8-битная палитра GIF
** чёрно-белые цветовые схемы
* Названия файлов строго без пробелов

## Зависимости
* asgiref==3.4.1
* certifi==2021.5.30
* charset-normalizer==2.0.5
* Django==3.2.7
* djangorestframework==3.12.4
* idna==3.2
* llvmlite==0.37.0
* numpy==1.20.3
* Pillow==8.3.2
* pytz==2021.1
* requests==2.26.0
* sqlparse==0.4.1
* urllib3==1.26.6


