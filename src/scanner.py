import os
import sys

def walk_dir(path, prefix="", ext_filter=None, verbose=False):

    files_count = 0
    dirs_count = 0
    total_size = 0
    file_list = []

    try:
        entries = sorted(os.listdir(path))
    except PermissionError:
        print(f"Нет доступа к {path}", file=sys.stderr)
        return 0, 0, 0, []

    for index, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        is_last = (index == len(entries) - 1)
        connector = "└── " if is_last else "├── "

        if os.path.isdir(full_path):
            dirs_count += 1
            if verbose:
                print(prefix + connector + entry + "/")
            sub_files, sub_dirs, sub_size, sub_file_list = walk_dir(
                full_path,
                prefix + ("    " if is_last else "│   "),
                ext_filter,
                verbose
            )
            files_count += sub_files
            dirs_count += sub_dirs
            total_size += sub_size
            file_list.extend(sub_file_list)
        else:
            if ext_filter is not None:
                if not entry.lower().endswith('.' + ext_filter.lower()):
                    continue
            files_count += 1
            file_size = os.path.getsize(full_path)
            total_size += file_size
            file_list.append(full_path)
            if verbose:
                print(prefix + connector + entry + f" ({file_size} байт)")

    return files_count, dirs_count, total_size, file_list