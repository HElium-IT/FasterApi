import sys
import typing
from typing import Callable

import typer

ExceptionType = 'typing.Type[Exception]'
ErrorHandlingCallback = Callable[[Exception], int]


class ErrorHandlingTyper(typer.Typer):
    error_handlers: typing.Dict[
        ExceptionType,
        ErrorHandlingCallback
    ] = {}

    def error_handler(self, exc: ExceptionType):
        def decorator(f: ErrorHandlingCallback,):
            self.error_handlers[exc] = f
            return f

        return decorator

    def __call__(self, *args, **kwargs):
        try:
            super(ErrorHandlingTyper, self).__call__(*args, **kwargs)
        except Exception as e:
            try:
                callback = self.error_handlers[type(e)]
                exit_code = callback(e)
                raise typer.Exit(code=exit_code)
            except typer.Exit as e:
                sys.exit(e.exit_code)
            except KeyError:
                raise