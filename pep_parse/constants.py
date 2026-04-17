from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
PEP_LINKS = 'a.pep::attr(href)'
TITLE = 'h1::text'
TITLE_ALL = 'h1 *::text'
STATUS_XPATH = (
    '//dt[contains(text(), "Status")]/'
    'following-sibling::dd[1]//text()'
)
STATUS_SUMMARY_FILE = 'status_summary_{}.csv'
CSV_HEADER = 'Статус,Количество\n'
TOTAL = 'Total'
NUMBER = 'number'
NAME = 'name'
STATUS = 'status'
