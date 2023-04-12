from django.db import models


class UserApp(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return str(self.id)


class Category(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(UserApp, on_delete=models.CASCADE)
    create_at = models.IntegerField(default=0)
    modified_at = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


class Card(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True, unique=True)
    color_start = models.IntegerField(default=0)
    color_end = models.IntegerField(default=0)
    count_open = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    card_base_info = models.CharField(max_length=255)
    card_second_info = models.CharField(max_length=255)
    type_base = models.IntegerField(default=0)
    value_base = models.CharField(max_length=255)
    exist_secondary = models.BooleanField(default=False)
    type_secondary = models.IntegerField(default=0)
    value_secondary = models.CharField(max_length=255)
    created_at = models.IntegerField(default=0)
    modified_at = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)

        # self.server_category_id = item['serverCategoryId']
        # self.created_at = item['createdAt']
        # self.modified_at = item['modifiedAt']
