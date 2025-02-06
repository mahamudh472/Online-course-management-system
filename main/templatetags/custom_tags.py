from django import template

register = template.Library()


@register.filter('get_keywords')
def get_keywords(obj):
    keywords = obj.keywords.split('-')
    return keywords


@register.filter('get_features')
def get_features(obj):
    features = obj.features.split('-')
    return features
