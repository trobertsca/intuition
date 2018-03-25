from pyintuition import Intuition

class Application(object):
    def __init__(self, **kwargs):
        self.name: str = kwargs['name']
        self.desc: str = kwargs.pop('desc', None)
        self.original: dict = kwargs['original']
        self.variables: dict = kwargs.pop('variables', None)
        self.chdbids: dict = kwargs['chdbids']
        self.fields: dict = kwargs['fields']

    @classmethod
    def get(cls, app_id: str, client: Intuition):
        schema = client.get_schema(app_id)
        return cls(**schema['table'])
