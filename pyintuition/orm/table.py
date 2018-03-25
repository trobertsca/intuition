from pyintuition import Intuition

class Table(object):
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.original = kwargs['original']
        self.queries = kwargs['queries']
        self.fields = kwargs['fields']
    
    @classmethod
    def get(cls, table_id: str, client: Intuition):
        schema = client.get_schema(table_id)
        return cls(**schema['table'])
