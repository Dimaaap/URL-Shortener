from .filters import EqualFilter


def get_data_from_model(model: callable, field: str, value):
    eq_filter = EqualFilter()
    return model.objects.get(**eq_filter(field, value))
