# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Как работает
main.py использует файл drinks_catalog.xlsx. В файле drinks_catalog.xlsx содержится ассортимент
напитков, которые будут выводиться на странице. 

## Запуск

- Скачайте код и перейдите в папку проекта:
```
git clone https://github.com/alexdiptan/dvmn_django_wine-shop.git
cd dvmn_django_wine-shop
```
- Создайте виртуальное окружение и активируйте его:
```
python3 -m venv my_env
source my_env/bin/activate
```
- установите зависимости:
```
pip install -r requirements.txt
```
- Запустите сайт командой 
```
python3 main.py
```
- После запуска, сгенерируется страница index.html
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
