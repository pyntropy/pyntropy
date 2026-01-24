from pathlib import Path
import logging

# Конфигурация путей
LOGS_DIR = Path("logs")
LOG_FILE = LOGS_DIR / "app.log"

# Создание директории логов
try:
    LOGS_DIR.mkdir(exist_ok=True)
except OSError as e:
    print(f"Ошибка при создании директории логов: {e}")
    raise

# Настройка файлового обработчика
file_handler = logging.FileHandler(LOG_FILE, mode='w', encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(
    fmt='%(asctime)s : %(levelname)s %(name)s -> %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
))

# Настройка корневого логгера
logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger().addHandler(file_handler)

# Создание логгера для приложения
log = logging.getLogger(__name__)