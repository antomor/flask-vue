import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from app.api.models import *

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def seed():
    "Add seed data to the database."
    text_type = RiskFieldType(name='text')
    text_type.save()
    number_type = RiskFieldType(name='number')
    number_type.save()
    date_type = RiskFieldType(name='date')
    date_type.save()
    
    sex_type = RiskFieldType(name='enum_sex')
    sex_type.save()

    sex_values = [
        RiskFieldEnumValue(risk_field_type_id=sex_type.id, value='M'),
        RiskFieldEnumValue(risk_field_type_id=sex_type.id, value='F')
    ]
    for s in sex_values:
        s.save()
    
    auto_r = RiskType(name='automobile', description='Risk linked to a vehicle')
    auto_r.save()
    auto_fields = [
        RiskField(name='person age', risk_type_id=auto_r.id, value='23', risk_field_type_id=number_type.id),
        RiskField(name='address', risk_type_id=auto_r.id, value='Regent street, London', risk_field_type_id=text_type.id),
        RiskField(name='birth_date', risk_type_id=auto_r.id, value='2018-01-23', risk_field_type_id=date_type.id),
        RiskField(name='sex', risk_type_id=auto_r.id, value='F', risk_field_type_id=sex_type.id)
    ]
    for f in auto_fields:
        f.save()

    house_r = RiskType(name='house', description='Risk linked to a house')
    house_r.save()
    house_fields = [
        RiskField(name='person age', risk_type_id=house_r.id, value='23', risk_field_type_id=number_type.id),
        RiskField(name='address', risk_type_id=house_r.id, value='50th Avenue, New York', risk_field_type_id=text_type.id),
        RiskField(name='birth_date', risk_type_id=house_r.id, value='2018-12-31', risk_field_type_id=date_type.id),
        RiskField(name='sex', risk_type_id=house_r.id, value='M', risk_field_type_id=sex_type.id)
    ]
    for f in house_fields:
        f.save()
    

def main():
    manager.run()


if __name__ == '__main__':
    main()
