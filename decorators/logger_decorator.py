from functools import wraps


def log_operation(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(
            f"[INFO] Ejecutando {func.__name__}"
        )

        result = func(*args, **kwargs)

        print(
            f"[INFO] Finalizado {func.__name__}"
        )

        return result

    return wrapper