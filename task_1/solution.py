from inspect import signature


def strict(func):
    def wrapper(*args, **kwargs):
        sig = signature(func)
        annotations = func.__annotations__
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        for name, value in bound_args.arguments.items():
            expected_type = annotations.get(name)
            if expected_type and not isinstance(value, expected_type):
                raise TypeError(
                    f"Argument '{name}' must be of type {expected_type.__name__}, got {type(value).__name__}"
                )

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(sum_two(1, 2))
    print(sum_two(1, 2.4))
