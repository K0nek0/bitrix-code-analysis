import os


def count_php_metrics(modules_dir, module_names=None):
    total_files = 0
    total_lines = 0
    total_size = 0

    if module_names is None:
        # Считать все подкаталоги в modules_dir
        paths_to_scan = [os.path.join(modules_dir, name) for name in os.listdir(modules_dir)
                         if os.path.isdir(os.path.join(modules_dir, name))]
    else:
        # Считать только указанные модули
        paths_to_scan = [os.path.join(modules_dir, name) for name in module_names
                         if os.path.isdir(os.path.join(modules_dir, name))]

    for path in paths_to_scan:
        for root, _, files in os.walk(path):
            for f in files:
                if f.endswith(".php"):
                    filepath = os.path.join(root, f)
                    try:
                        total_files += 1
                        total_size += os.path.getsize(filepath)
                        with open(filepath, "r", encoding="utf-8", errors="ignore") as fp:
                            total_lines += sum(1 for _ in fp)
                    except Exception:
                        pass  # Игнорировать ошибки чтения

    return total_files, total_lines, total_size


MODULES_PATH = "bitrix-core-business/modules"

# Для "Бизнес" (все модули)
files_b, lines_b, size_b = count_php_metrics(MODULES_PATH)

# Для "Старт" (сопоставляю наиболее вероятные папки)
START_MODULES = {
    "main", "iblock", "search", "highloadblock", "translate", "landing",
    "seo", "socialservices", "b24connector", "perfmon", "clouds", "security", "mobileapp"
}
files_s, lines_s, size_s = count_php_metrics(MODULES_PATH, START_MODULES)

# Вывод
print("Бизнес:")
print(f"  Файлов: {files_b}")
print(f"  Строк: {lines_b}")
print(f"  Байт: {size_b}")

print("\nСтарт:")
print(f"  Файлов: {files_s}")
print(f"  Строк: {lines_s}")
print(f"  Байт: {size_s}")
