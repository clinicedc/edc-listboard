import urllib


class ListboardFilter:
    def __init__(
        self,
        name=None,
        label=None,
        lookup=None,
        exclude_filter=None,
        default=None,
        position=None,
    ):
        self.name = name
        self.label = label or name
        self.position = position or 0
        self.exclude_filter = exclude_filter
        if exclude_filter:
            self.attr = "e"
        else:
            self.attr = "f"
        self.lookup = lookup or {}
        self.default = default

    def __repr__(self):
        return (
            "{0.__class__.__name__}({0.name}, {0.label}, "
            "exclude_filter={0.exclude_filter}, {0.default})".format(self)
        )

    @property
    def querystring(self):
        return urllib.parse.urlencode({self.attr: self.name})

    @property
    def lookup_options(self):
        lookup_options = {}
        for k, v in self.lookup.items():
            try:
                lookup_options.update({k: v()})
            except TypeError:
                lookup_options.update({k: v})
        return lookup_options
