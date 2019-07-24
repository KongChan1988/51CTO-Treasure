# -*- coding:utf-8 -*-
# Author:D.Gray
from django import template
register = template.Library()
@register.simple_tag
def kyo(a1,a2):
    return a1+a2

@register.filter
def mary(a1,a2):
    return a1+a2