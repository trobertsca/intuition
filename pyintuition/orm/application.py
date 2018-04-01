from pyintuition import Intuition

class Application(object):
    objects = []

    def __init__(self, **kwargs):
        self.name: str = kwargs['name']
        self.desc: str = kwargs.pop('desc', None)
        self.original: dict = kwargs['original']
        self.variables: dict = kwargs.pop('variables', None)
        self.chdbids: dict = kwargs['chdbids']['chdbid']
        self.fields: dict = kwargs['fields']

        self.client = kwargs['client']

        self.tables = []

        Application.objects.append(self)

    @classmethod
    def get(cls, app_id: str, client: Intuition):
        schema = client.get_schema(app_id)
        return cls(**schema['table'], client=client)
