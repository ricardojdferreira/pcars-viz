from elasticsearch import Elasticsearch

class Elastic(Elasticsearch):
    def __init__(self):
        
        # Start elasticsearch connection - delete index pcars2 if exists
        self._instance = Elasticsearch(hosts="192.168.1.101") # TODO: dynaminc IP
        self._instance.indices.delete(index='pcars2', ignore=[400, 404])
        self._instance.indices.create(index='pcars2', ignore=[400, 404])

        # Add mapping for specific type fields
        mapping = ""
        with open("./elastic_api_mapping", "r") as file:
            for line in file:
                mapping += line
        self._instance.indices.put_mapping(index='pcars2', body=mapping)