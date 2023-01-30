

class Utils:
    @staticmethod
    def get_or_defauls(d: dict[str, 'Any'], key: str, default):
        data = d.get(key)
        if data is None:
            return default
        return data
