import argparse

def get_parser():
    parser = argparse.ArgumentParser(
        description="Базовый индексатор папок (без SQLite, дубликатов и бэкапа).",
        epilog="Пример: python -m src.main /путь/к/папке -e txt -o my_report.txt -v"
    )
    parser.add_argument(
        "path",
        help="Путь к папке для сканирования"
    )
    parser.add_argument(
        "-e", "--ext",
        default=None,
        help="Фильтр по расширению (например, 'txt', 'py'). Если не указан — все файлы."
    )
    parser.add_argument(
        "-o", "--output",
        default="report.txt",
        help="Имя файла для сохранения отчёта (по умолчанию report.txt)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Показывать дерево файлов и папок в консоли"
    )
    return parser