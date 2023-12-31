from argparse import Action, ArgumentTypeError
import validators


class ValidateUrl(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        if not validators.url(values[0]):
            raise ArgumentTypeError('{} is not URL'.format(values[0]))
        namespace.__setattr__(self.dest, values[0])
