class CategoryWithCards:
    def __init__(self, item):
        self.category = ClientCategories(item)
        self.cards = []
        for i in range(0, len(item['cards'])):
            self.cards.append(ClientCards(item['cards'][i]))


class ClientCategories:
    def __init__(self, item):
        self.name = item['name']
        self.server_category_id = item['serverCategoryId']
        self.created_at = item['createdAt']
        self.modified_at = item['modifiedAt']


class ClientCards:
    def __init__(self, item):
        self.server_card_id = item['serverCardId']
        self.category_id = item['categoryId']
        self.color_start = item['colorStart']
        self.color_end = item['colorEnd']
        self.count_open = item['countOpen']
        self.count_open = item['countOpen']
        self.name = item['name']
        self.card_base_info = item['cardBaseInfo']
        self.card_second_info = item['cardSecondInfo']
        self.type_base = item['typeBase']
        self.value_base = item['valueBase']
        self.exist_secondary = item['existSecondary']
        self.type_secondary = item['typeSecondary']
        self.value_secondary = item['valueSecondary']
        self.created_at = item['createdAt']
        self.modified_at = item['modifiedAt']
