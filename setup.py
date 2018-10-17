from model import db, Participant, Prize_Structure, Team

db.connect()

# This line will allow you "upgrade" an existing database by
# dropping all existing tables from it.
db.drop_tables([Participant, Prize_Structure, Team])

db.create_tables([Participant, Prize_Structure, Team])

play_in = Prize_Structure(advanced_to_round=0, money_share=0).save()
first = Prize_Structure(advanced_to_round=1, money_share=0).save()
second = Prize_Structure(advanced_to_round=2, money_share=0).save()
sweet_sixteen = Prize_Structure(advanced_to_round=3, money_share=0.03).save()
elite_eight = Prize_Structure(advanced_to_round=4, money_share=0.05).save()
final_four = Prize_Structure(advanced_to_round=5, money_share=0.1).save()
championship = Prize_Structure(advanced_to_round=6, money_share=0.16).save()
winner = Prize_Structure(advanced_to_round=7, money_share=0.2).save()

teams = [('Villanova', 'East', 1, first),
         ('Michigan', 'West', 3, first),
         ('Kansas', 'Midwest', 1, first),
         ('Loyola (IL)', 'South', 11, first),
         ('Kansas State', 'South', 9, first),
         ('Florida State', 'West', 9, first),
         ('Duke', 'Midwest', 2, first),
         ('Texas Tech', 'East', 3, first),
         ('Kentucky', 'South', 5, first),
         ('Nevada', 'South', 7, first),
         ('Gonzaga', 'West', 4, first),
         ('Texas A&M', 'West', 7, first),
         ('Clemson', 'Midwest', 5, first),
         ('Syracuse', 'Midwest', 11, play_in),
         ('W. Virginia', 'East', 5, first),
         ('Purdue', 'East', 2, first),
         ('Marshall', 'East', 13, first),
         ('UMBC', 'South', 16, first),
         ('Buffalo', 'South', 13, first),
         ('Tennessee', 'South', 3, first),
         ('Cincinnati', 'South', 2, first),
         ('Xavier', 'West', 1, first),
         ('Ohio State', 'West', 5, first),
         ('Houston', 'West', 6, first),
         ('UNC', 'West', 2, first),
         ('Seton Hall', 'Midwest', 8, first),
         ('Auburn', 'Midwest', 4, first),
         ('Michigan St.', 'Midwest', 3, first),
         ('Rhode Island', 'Midwest', 7, first),
         ('Alabama', 'East', 9, first),
         ('Florida', 'East', 6, first),
         ('Butler', 'East', 10, first),
         ('Virginia', 'South', 1, first),
         ('Creighton', 'South', 8, first),
         ('Davidson', 'South', 12, first),
         ('Arizona', 'South', 4, first),
         ('Miami', 'South', 6, first),
         ('Wright State', 'South', 14, first),
         ('Texas', 'South', 10, first),
         ('Georgia St.', 'South', 15, first),
         ('TXSO', 'West', 16, play_in),
         ('Missouri', 'West', 8, first),
         ('S. Dakota St.', 'West', 12, first),
         ('UNC-Greens.', 'West', 13, first),
         ('SDSU', 'West', 11, first),
         ('Montana', 'West', 14, first),
         ('Providence', 'West', 10, first),
         ('Lipscomb', 'West', 15, first),
         ('Penn', 'Midwest', 16, first),
         ('NC State', 'Midwest', 9, first),
         ('NM State', 'Midwest', 12, first),
         ('Charleston', 'Midwest', 13, first),
         ('TCU', 'Midwest', 6, first),
         ('Bucknell', 'Midwest', 14, first),
         ('Oklahoma', 'Midwest', 10, first),
         ('Iona', 'Midwest', 15, first),
         ('Radford', 'East', 16, play_in),
         ('Virginia Tech', 'East', 8, first),
         ('Murray St.', 'East', 12, first),
         ('Wichita St.', 'East', 4, first),
         ('St. Bon.', 'East', 11, play_in),
         ('SF Austin', 'East', 14, first),
         ('Arkansas', 'East', 7, first),
         ('CSU-Full.', 'East', 15, first),
         ('NC Central', 'West', 16, play_in),
         ('Arizona St.', 'Midwest', 11, play_in),
         ('Long Island', 'East', 16, play_in),
         ('UCLA', 'East', 11, play_in)]

for college in teams:
    Team(team=college[0],
         seed=college[2],
         region=college[1],
         advanced_to_round=college[3],
         price=0,
         money_award=0,
         owner='TBD')
