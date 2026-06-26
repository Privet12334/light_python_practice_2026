import os
import sys

def validate_path(path):
    """Проверяет, что путь существует и является папкой."""
    if not os.path.exists(path):
        print(f"Ошибка: путь '{path}' не существует.", file=sys.stderr)
        sys.exit(1)
    if not os.path.isdir(path):
        print(f"Ошибка: '{path}' не является папкой.", file=sys.stderr)
        sys.exit(1)
    return os.path.abspath(path)

def sizeof_fmt(num, suffix='Б'):
    """Форматирует размер в байтах в читаемый вид (опционально)."""
    for unit in ['', 'К', 'М', 'Г']:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f} Т{suffix}"