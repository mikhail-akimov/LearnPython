import log_config


def log(msg):
    def log_add(func):
        def wrapper(*args, **kwargs):
            log_config.logger.info(msg)
            func(*args, **kwargs)
        return wrapper
    return log_add

# test