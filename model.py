import os

from peewee import Model, CharField, IntegerField, DecimalField, ForeignKeyField
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))

class BaseModel(Model):
    class Meta:
        database = db


class Participant(BaseModel):
    full_name = CharField(primary_key=True, max_length=60)
    points_spent = IntegerField()
    total_buy_in = IntegerField()
    money_earned = DecimalField()
    net_gain_loss = DecimalField()


class Prize_Structure(BaseModel):
    advanced_to_round = IntegerField()
    money_share = DecimalField()


class Team(BaseModel):
    team = CharField(max_length=60)
    seed = IntegerField()
    region = CharField(max_length=7)
    advanced_to_round = ForeignKeyField(Prize_Structure, related_name='made it to round', null=False)
    price = IntegerField()
    money_award = DecimalField()
    owner = ForeignKeyField(Participant, related_name='bought by', null=False)
