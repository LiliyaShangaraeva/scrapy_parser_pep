import datetime as dt
from collections import defaultdict

from pep_parse.constants import (BASE_DIR, DATETIME_FORMAT, STATUS, RESULTS,
                                 STATUS_SUMMARY_FILE, CSV_HEADER, TOTAL)


class PepParsePipeline:
    """Pipeline для подсчёта количества PEP по статусам."""

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
        results_dir = BASE_DIR / RESULTS
        results_dir.mkdir(parents=True, exist_ok=True)

        total = sum(self.status_counter.values())
        filename = results_dir / STATUS_SUMMARY_FILE.format(
            dt.datetime.now().strftime(DATETIME_FORMAT)
        )

        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(CSV_HEADER)

            for status, count in self.status_counter.items():
                f.write(f'{status},{count}\n')

            f.write(f'{TOTAL},{total}\n')
