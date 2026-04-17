# PEP Parser
Парсер для сбора информации о PEP с официального сайта с помощью Scrapy.

## Описание проекта

Собирает список всех PEP на https://peps.python.org/
Извлекает:
- номер (number)
- название (name)
- статус (status) — берётся со страницы каждого PEP

Сохраняет данные в два CSV-файла:
1. pep_*.csv — полный список PEP (через Scrapy Feeds)
2. status_summary_*.csv — сводка по количеству PEP в каждом статусе (через кастомный Pipeline)

---

## Технологический стек

Python 3.12+

BeautifulSoup4

requests-cache

tqdm

prettytable

---

## Как развернуть проект

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/LiliyaShangaraeva/scrapy_parser_pep
cd scrapy_parser_pep
```

### 2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Установите зависимости:

```bash
pip install -r requirements.txt
```

### 4. Запустите парсер:

```bash
scrapy crawl pep

```

### Формат pep_*.csv:

```bash
number,name,status
1,Python Unicode Integration,Active
201,Lockstep Iteration,Final
...
```

### Формат status_summary_*.csv:

```bash
Статус,Количество
Active,37
Final,352
Rejected,128
...
Total,725
```

### Автор:
[Лилия Шангараева](https://github.com/LiliyaShangaraeva)
