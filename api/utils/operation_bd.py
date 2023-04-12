from api.entity.client_entity import CategoryWithCards, ClientCards
from api.models import *


def update_bd(categories_client, user_email):
    for i in range(0, len(categories_client)):
        update_categories(categories_client[i], user_email)
    return


def get_user(user_email):
    user = UserApp.objects.filter(email=user_email)
    if not user:
        user = UserApp.objects.create(email=user_email)
    else:
        user = UserApp.objects.get(email=user_email)
    return user


def update_categories(client_category: CategoryWithCards, user_email: str):
    category = Category.objects.filter(user__email=user_email, name=client_category.category.name)
    if not category:
        user = get_user(user_email)
        category = Category.objects.create(user=user,
                                           name=client_category.category.name,
                                           create_at=client_category.category.created_at,
                                           modified_at=client_category.category.modified_at)
    else:
        category = Category.objects.get(user__email=user_email, name=client_category.category.name)
    for i in range(0, len(client_category.cards)):
        create_or_update_card(client_category.cards[i], category)


def create_or_update_card(data: ClientCards, category: Category):
    card = Card.objects.filter(id=data.server_card_id)
    if not card:
        Card.objects.create(
            color_start=data.color_start,
            color_end=data.color_end,
            count_open=data.count_open,
            name=data.name,
            card_base_info=data.card_base_info,
            card_second_info=data.card_second_info,
            type_base=data.type_base,
            value_base=data.value_base,
            exist_secondary=data.exist_secondary,
            type_secondary=data.type_secondary,
            value_secondary=data.value_secondary,
            created_at=data.created_at,
            modified_at=data.modified_at,
            category=category)
