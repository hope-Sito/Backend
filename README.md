# Backend
Это мини-монорепа. Слава монорепам!
## Установка для dev:
### Требования
1) Необходим установленный python3.11
2) Для управления зависимостями используется poetry
3) ...
### Установка
1) Установка зависимостей:
```bash
poetry install --no-root
pip install pre-commit
```
2) Накатывание миграций:
```bash
alembic upgrade head
```
3) Установка pre-commit:
```bash
pre-commit install
```
4) Создание `.env` (пример заполнения лежит в `.env.template`)
```bash
cat .env.template > .env
```
### Запуск
1) Запуск API сервиса для клиентов
...
2) Запуск API сервис для датчиков
...
3) Запуск celery-worker'а
...
4) Запуск админки
...
### Тестирование
```bash
pytest sputnik -s
```
