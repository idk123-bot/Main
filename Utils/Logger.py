# Utils/Logger.py
import logging
import os


def setup_logging():
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(script_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    log_path = os.path.join(data_dir, "bot.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )
    return logging.getLogger()


logger = setup_logging()
