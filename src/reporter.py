from datetime import datetime

def generate_report(path, ext_filter, files_count, dirs_count, total_size, file_list):
    """Формирует строку отчёта."""
    lines = []
    lines.append("=" * 60)
    lines.append("ОТЧЁТ О СКАНИРОВАНИИ ПАПКИ (базовый вариант)")
    lines.append("=" * 60)
    lines.append(f"Путь: {path}")
    lines.append(f"Дата сканирования: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Фильтр: {'.' + ext_filter if ext_filter else 'все файлы'}")
    lines.append("-" * 60)
    lines.append(f"Количество папок:          {dirs_count}")
    lines.append(f"Количество файлов:         {files_count}")
    lines.append(f"Общий размер всех файлов:  {total_size} байт")
    if files_count > 0:
        avg_size = total_size / files_count
        lines.append(f"Средний размер файла:     {avg_size:.2f} байт")
    lines.append("-" * 60)
    lines.append("СПИСОК ОТОБРАННЫХ ФАЙЛОВ:")
    if file_list:
        for f in sorted(file_list):
            lines.append(f"  {f}")
    else:
        lines.append("  (нет файлов, удовлетворяющих фильтру)")
    lines.append("=" * 60)
    return "\n".join(lines)

def save_report(report, output_file):
    """Сохраняет отчёт в текстовый файл."""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report)