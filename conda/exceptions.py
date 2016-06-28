from __future__ import absolute_import, division, print_function


class CondaError(Exception):
    def __init__(self, *args, **kwargs):
        super(CondaError, self).__init__(*args, **kwargs)

    def __repr__(self):
        return ' '.join([str(arg)+'\n' for arg in self.args if not isinstance(arg, bool)])


class InvalidInstruction(CondaError):
    def __init__(self, instruction, *args, **kwargs):
        msg = "No handler for instruction: %r" % instruction
        super(InvalidInstruction, self).__init__(msg, *args, **kwargs)


class LockError(CondaError, RuntimeError):
    pass


class ArgumentError(CondaError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Argument Error: %s' % message
        super(ArgumentError, self).__init__(msg, *args, **kwargs)


class ArgumentNotFoundError(ArgumentError):
    def __init__(self, argument, *args, **kwargs):
        msg = 'Argument not found: %r' % argument
        super(ArgumentNotFoundError, self).__init__(msg, *args, **kwargs)


class TooManyArgumentsError(ArgumentError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Too many arguments: %s' % message
        super(TooManyArgumentsError, self).__init__(msg, *args, **kwargs)


class TooFewArgumentsError(ArgumentError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Too few arguments: %s' % message
        super(TooFewArgumentsError, self).__init__(msg, *args, **kwargs)


class CommandError(CondaError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Command Error: %s' % message
        super(CommandError, self).__init__(msg, *args, **kwargs)


class CommandNotFoundError(CommandError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Command not found: %s' % message
        super(CommandNotFoundError, self).__init__(msg, *args, **kwargs)


class CondaFileNotFoundError(CondaError, FileNotFoundError):
    def __init__(self, message, *args, **kwargs):
        msg = "File not found: %s" % message
        super(CondaFileNotFoundError, self).__init__(msg, *args, **kwargs)


class DirectoryNotFoundError(CondaError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Directory not found: %s' % message
        super(DirectoryNotFoundError, self).__init__(msg, *args, **kwargs)


class CondaEnvironmentError(CondaError, EnvironmentError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Environment not found: %s' % message
        super(CondaEnvironmentError, self).__init__(msg, *args, **kwargs)


class DryRunExit(CondaError):
    def __init__(self, *args, **kwargs):
        msg = 'Dry run: exiting'
        super(DryRunExit, self).__init__(msg, *args, **kwargs)


class CondaSystemExit(CondaError, SystemExit):
    def __init__(self, message, *args, **kwargs):
        msg = 'Exiting: %s' % message
        super(CondaSystemExit, self).__init__(msg, *args, **kwargs)


class SubprocessExit(CondaError):
    def __init__(self, *args, **kwargs):
        msg = 'Subprocess exiting: '
        super(SubprocessExit, self).__init__(msg, *args, **kwargs)


class PaddingError(CondaError):
    def __init__(self, *args, **kwargs):
        msg = 'Padding error: '
        super(PaddingError, self).__init__(msg, *args, **kwargs)


class LinkError(CondaError):
    def __init__(self, *args, **kwargs):
        msg = 'Link error: '
        super(LinkError, self).__init__(msg, *args, **kwargs)


class CondaOSError(CondaError, OSError):
    def __init__(self, message, *args, **kwargs):
        msg = 'OS error: %s' % message
        super(CondaOSError, self).__init__(msg, *args, **kwargs)


class AlreadyInitializedError(CondaError):
    def __init__(self, message, *args, **kwargs):
        super(AlreadyInitializedError, self).__init__(message, *args, **kwargs)


class ProxyError(CondaError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Proxy error: %s' % message
        super(ProxyError, self).__init__(msg, *args, **kwargs)


class CondaIOError(CondaError, IOError):
    def __init__(self, message, *args, **kwargs):
        msg = 'IO error: %s' % message
        super(CondaIOError, self).__init__(msg, *args, **kwargs)


class CondaFileIOError(CondaIOError):
    def __init__(self, message, *args, **kwargs):
        msg = "Couldn't read or write to file. %s" % message
        super(CondaFileIOError, self).__init__(msg, *args, **kwargs)


class CondaKeyError(CondaError, KeyError):
    def __init__(self, message, *args, **kwargs):
        self.msg = 'Key error: %s' % message
        super(CondaKeyError, self).__init__(self.msg, *args, **kwargs)

    def __repr__(self):
        return self.msg


class ChannelError(CondaError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Channel Error: %s' % message
        super(ChannelError, self).__init__(msg, *args, **kwargs)


class ChannelNotAllowed(ChannelError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Channel not allowed: %s' % message
        super(ChannelNotAllowed, self).__init__(msg, *args, **kwargs)


class CondaImportError(CondaError, ImportError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Import error: %s' % message
        super(CondaImportError, self).__init__(msg, *args, **kwargs)


class ParseError(CondaError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Parse error: %s' % message
        super(ParseError, self).__init__(msg, *args, **kwargs)


class MD5MismatchError(CondaError):
    def __init__(self, message, *args, **kwargs):
        msg = 'MD5MismatchError: %s' % message
        super(MD5MismatchError, self).__init__(msg, *args, **kwargs)


class PackageNotFoundError(CondaError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Package not found: %s' % message
        super(PackageNotFoundError, self).__init__(msg, *args, **kwargs)


class InstallError(CondaError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Install error: %s' % message
        super(InstallError, self).__init__(msg, *args, **kwargs)


class RemoveError(CondaError):
    def __init__(self, message, *args, **kwargs):
        msg = 'RemoveError: %s' % message
        super(RemoveError, self).__init__(msg, *args, **kwargs)


class CondaIndexError(CondaError, IndexError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Index error: %s' % message
        super(CondaIndexError, self).__init__(msg, *args, **kwargs)


class CondaRuntimeError(CondaError, RuntimeError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Runtime error: %s' % message
        super(CondaRuntimeError, self).__init__(msg, *args, **kwargs)


class CondaValueError(CondaError, ValueError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Value error: %s' % message
        super(CondaValueError, self).__init__(msg, *args, **kwargs)


class CondaTypeError(CondaError, TypeError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Type error: %s' % message
        super(CondaTypeError, self).__init__(msg, *args, **kwargs)


class CondaAssertionError(CondaError, AssertionError):
    def __init__(self, message, *args, **kwargs):
        msg = 'Assertion error: %s' % message
        super(CondaAssertionError, self).__init__(msg, *args, **kwargs)


def conda_exception_handler(func, *args, **kwargs):
    try:
        return_value = func(*args, **kwargs)
        if isinstance(return_value, int):
            return return_value
    except CondaError as e:
        from conda.config import output_json
        from conda.cli.common import stdout_json
        from sys import stderr

        message = repr(e)

        if output_json:
            stdout_json(dict(error=message))
        else:
            stderr.write(message)

        return 1
