# Quality Assurance / Обеспечение качества при разработке ПО
## ДЗ №4: автотесты по чек-листам. Selenium Webdriver + python, pytest + chrome

### Требования:  
- python, pytest, selenium, chrome
- все тесты должны запускаться одной командой, а именно ./runner_tests.sh (заглушка уже есть в репозитории)
- весь код пишем в дирректории ../hw/code, иначе заглушка для запука не сработает
- все тесты должны проходить
- не должно быть антипаттернов тестирования
- использование паттерна PageObject
- запуск локально и прохождение в chrome
----
## Тестируемый проект: [Агрегатор ресторанов](https://github.com/Natali-Skv/backend_2_sem_techknopark) 

## Чек-листы функциональных тестов (80 тестов)
- [Шапка, главная страница, поиск ресторана, выбор адреса, страница истории заказов](https://github.com/Natali-Skv/technopark_qa_homework-3/blob/main/VVT-i-Natali-Skvortsova.md)
- [Страница ресторана с товарами, Корзина, Рекомендации, Промокоды, Отзывы на ресторан](https://github.com/Natali-Skv/technopark_qa_homework-3/blob/main/VVT-i-Sergey-Glubev.md)
- [Cтраницы авторизации, регистрации, подтверждения кода, профиля, заказа и выход из аккаунта](https://github.com/Natali-Skv/technopark_qa_homework-3/blob/main/VVT-i-Kirill-Katashinsky.md.md)

---
## Результаты тестирования: 
![](https://user-images.githubusercontent.com/71991158/230614998-07defa07-030a-4996-8407-4b70fccfd73e.png)
*"s" – skipped, данный тест стабильно не проходит, так как webdriver не видит необходимый элемент по непонятным причинам (элемент на странице присутствует и через инструменты разработчика обнаруживается ожидаемым образом). Были проверены многие из возможных причин, но проблема не была найдена. В том числе использовались инструменты дебага* 

---

## Запуск тестов
1. **Настраиваем окружение.**
```
python3 -m venv venv
source venv/bin/activate
```

2. **Устанавливаем зависимости.**
```
pip install -r requirements.txt
```

3. **Устанавливаем пакеты.**
- **Ubuntu:**
```
sudo apt-get install python3-tk python3-dev
```
 - **MacOS:** 
```
brew install python-tk@3.9 python3-dev
```
4. **Запуск тестов**
```
./runner_tests.sh
```
