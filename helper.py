import logging


def method_is_callable(obj, method_name):

    try:
        return callable(getattr(obj, method_name))
    except Exception as exc:
        logging.exception(exc)
        exit("Something happend :( \nec2 out")
    finally:
        return None

def set_val_safe(data, field_name, is_set_null=False):
    field_value = ''
    try:
        field_value = data[field_name]
    except KeyError as exc:
        print('set_val_safe Exception -> ')
        print(exc)
        if is_set_null:
            field_value = None

    return field_value
