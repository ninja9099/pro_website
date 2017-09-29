from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    if type(dictionary) != dict:
        raise ValueError('filter can be used with dictionaries only')
    return dictionary.get(key)

# @register.filter
# def is_empty(check_list):
# 	if len(check_list)==0:
# 		return True
# 	else:
# 		return False