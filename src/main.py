#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from src.cli import get_parser
from src.utils import validate_path
from src.scanner import walk_dir
from src.reporter import generate_report, save_report

def main():
    parser = get_parser()
    args = parser.parse_args()

    abs_path = validate_path(args.path)

    if args.verbose:
        print(f"Сканирование папки: {abs_path}")
        print(f"Фильтр: {'.' + args.ext if args.ext else 'все файлы'}")
        print("\nСТРУКТУРА ПАПКИ:")
        print(os.path.basename(abs_path) + "/")

    files_count, dirs_count, total_size, file_list = walk_dir(
        abs_path,
        ext_filter=args.ext,
        verbose=args.verbose
    )

    report = generate_report(
        abs_path, args.ext,
        files_count, dirs_count, total_size, file_list
    )

    print("\n" + report)

    save_report(report, args.output)
    print(f"\nОтчёт сохранён в файл: {args.output}")

if __name__ == "__main__":
    main()