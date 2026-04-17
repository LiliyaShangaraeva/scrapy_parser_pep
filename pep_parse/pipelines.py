import csv
import datetime as dt
from collections import defaultdict

from pep_parse.constants import (DATETIME_FORMAT, STATUS, RESULTS_DIR,
                                 STATUS_SUMMARY_FILE, CSV_HEADER, TOTAL)


class PepParsePipeline:
    """Pipeline для подсчёта количества PEP по статусам."""

    def __init__(self):
        RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    def open_spider(self, spider):
        """Инициализирует счётчик статусов."""
        self.status_counter = defaultdict(int)

    def process_item(self, item, spider):
        """Увеличивает счётчик для каждого статуса."""
        status = item[STATUS]
        self.status_counter[status] += 1
        return item

    def close_spider(self, spider):
        """Создаёт CSV-файл со сводкой по статусам."""
        total = sum(self.status_counter.values())
        filename = RESULTS_DIR / STATUS_SUMMARY_FILE.format(
            dt.datetime.now().strftime(DATETIME_FORMAT)
        )

        rows = [
            tuple(CSV_HEADER.split(',')),
            *self.status_counter.items(),
            (TOTAL, total),
        ]

        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
