log_config = {
    "version": 1,
    "formatters": {
        "stream_formatter": {
            "format": "%(levelname)s %(message)s"
        },
        "file_formatter": {
            "format": "%(asctime)s %(levelname)s %(message)s",
            'datefmt': "%d-%m-%Y %H:%M:%S"
        },
    },
    "handlers": {
        "stream_handler": {
            "class": "logging.StreamHandler",
            "formatter": "stream_formatter",
            'stream': 'ext://sys.stdout'
        },
        "file_handler": {
            "class": "logging.FileHandler",
            "formatter": "file_formatter",
            "filename": "bot_log.log",
            "encoding": "UTF-8",
        },
    },
    "loggers": {
        "file": {
            "handlers": ["file_handler"],
            "level": "DEBUG",
        },
        "stream": {
            "handlers": ["stream_handler"],
            "level": "INFO",
        },
    },
}