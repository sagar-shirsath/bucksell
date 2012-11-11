from django import template
register = template.Library()


def two_decimal(value , arg): # Only one argument.
    return "%.02f" %value

register.filter('two_decimal', two_decimal)