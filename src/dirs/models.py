class Directory:
    def __init__(self, name, path, quick_access=None):
        self.name = name
        self.path = path
        self.quick_access = quick_access

    def to_dict(self):
        return vars(self)

    @staticmethod
    def schema():
        return ["name", "path", "quick_access"]
