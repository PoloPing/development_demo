import json
from itertools import chain


from django.core.serializers.json import DjangoJSONEncoder


def model_to_dict(instance, fields=None, exclude=None, localize=False):
    """
    Returns a dict containing the data in ``instance`` suitable for passing as
    a Form's ``initial`` keyword argument.

    ``fields`` is an optional list of field names. If provided, only the named
    fields will be included in the returned dict.

    ``exclude`` is an optional list of field names. If provided, the named
    fields will be excluded from the returned dict, even if they are listed in
    the ``fields`` argument.
    """
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields,
                   opts.many_to_many):
        if isinstance(fields, str) and fields == 'dump_all':
            data[f.name] = f.value_from_object(instance)
            continue
        if not getattr(f, 'editable', False):
            continue
        if fields and f.name not in fields:
            continue
        if exclude and f.name in exclude:
            continue
        data[f.name] = f.value_from_object(instance)
    return data


def dumps(msg):
    return json.dumps(msg, cls=DjangoJSONEncoder, ensure_ascii=False)


class ModelSerializeMixin:
    def to_dict(self, fields=None, exclude=None, localize=False):
        return model_to_dict(self, fields, exclude, localize)

    def dumps(self, fields=None, exclude=None, localize=False):
        serialized = self.to_dict(fields, exclude, localize)
        return dumps(serialized)

