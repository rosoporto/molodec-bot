import os
import json
import config
from utils.get_logger import logger as log


class HandlerJson():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self):
        self.json_file_name = config.DATA_USERS
        self._json_file = os.path.join(self.project_root, self.json_file_name)

    @property
    def load_data(self):
        try:
            with open(self._json_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            log.info("Файл users.json не найден, создаём новый")
            return {}
        except Exception as e:
            log.error(f"Ошибка при загрузке данных: {e}")
            return {}

    @load_data.setter
    def load_data(self, data):
        try:
            with open(self._json_file, "w") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            log.debug("Данные успешно сохранены в users.json")
        except Exception as e:
            log.error(f"Ошибка при сохранении данных: {e}")


if __name__ == "__main__":
    data = {
        "123456789": {
            "habit": "Пить воду",
            "progress": "",
            "day": 0,
            "last_date": ""
        },
    }

    handler_json = HandlerJson()
    print(f"handler_json: {handler_json.load_data}")

    handler_json.load_data = data
    print(f"handler_json: {handler_json.load_data}")
