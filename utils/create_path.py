import os


def create_path(path: str, file_name: str):
    from .get_logger import logger   # Ленивый импорт

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logs_dir = os.path.join(project_root, path)
    if not os.path.exists(logs_dir):
        logger.warning(f"{logs_dir} in not exists")
        os.makedirs(logs_dir)
        logger.info(f"{logs_dir} is created")

    return os.path.join(logs_dir, file_name)


def main():
    print(create_path("demo", "file.log"))


if __name__ == '__main__':
    main()