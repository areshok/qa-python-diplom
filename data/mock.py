from unittest.mock import Mock


def bun_mock():
    bun = Mock()
    bun.get_name.return_value = "булочка"
    bun.get_price.return_value = 404.0
    return bun


def ingridient_mock():
    ingridient = Mock()
    ingridient.get_price.return_value = 404.4
    ingridient.get_name.return_value = "колбаса"
    ingridient.get_type.return_value = "мясо"
    return ingridient


def ingridient_2_mock():
    ingridient = Mock()
    ingridient.get_price.return_value = 111.1
    ingridient.get_name.return_value = "ананас"
    ingridient.get_type.return_value = "фрукт"
    return ingridient
