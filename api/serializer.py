import json

from api.entity.client_entity import CategoryWithCards


def serialize_data(data):
    result = []
    list_items = json.loads(json.dumps(data))
    for i in range(0, len(list_items)):
        result.append(CategoryWithCards(list_items[i]))
    return result
