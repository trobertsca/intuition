from pyintuition import Intuition
from pyintuition.orm import Application

class Table(object):
    objects = []

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.original = kwargs['original']
        self.queries = kwargs['queries']
        self.fields = kwargs['fields']

        self.records = []

        Table.objects.append(self)
    
    @classmethod
    def get(cls, table_id: str, client: Intuition, application: Application):
        response = client.get_schema(table_id)
        table = cls(**response['table'])
        application.tables.append(table)
        return table
