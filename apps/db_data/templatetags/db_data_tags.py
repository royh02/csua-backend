import datetime

from django import template

from apps.db_data.models import Event, Notice

register = template.Library()


@register.simple_tag
def get_upcoming_events():
    return Event.objects.filter(start_time__gte=datetime.datetime.now())


@register.simple_tag
def get_current_notices():
    return Notice.objects.filter(expires__gte=datetime.date.today())
