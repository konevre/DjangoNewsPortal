from django import template
from profanity_filter import ProfanityFilter

register = template.Library()
pf = ProfanityFilter()

@register.filter()
def profanity(value):
    new_value = pf.censor(value)
    return f'{new_value}'