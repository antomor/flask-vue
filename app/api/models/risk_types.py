from app import db


class RiskType(db.Model):
    """ 
    It models a custom risk type
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(150), unique=False, nullable=True)
    fields = db.relationship('RiskField', backref='risk_type', lazy=True)

    @staticmethod
    def get_all():
        return RiskType.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        fields_serialized = [field.serialize() for field in self.fields]
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'fields': fields_serialized
        }


class RiskField(db.Model):
    """ 
    It models a single field of a custom risk
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    risk_type_id = db.Column(db.Integer, db.ForeignKey(
        'risk_type.id'), nullable=False)
    value = db.Column(db.String(150), nullable=True)
    risk_field_type_id = db.Column(db.Integer, db.ForeignKey(
        'risk_field_type.id'), nullable=False)
    risk_field_type = db.relationship('RiskFieldType')

    @staticmethod
    def get_all():
        return RiskField.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        enum_values = [
            enum_value.value for enum_value in self.risk_field_type.values]
        return {
            'id': self.id,
            'name': self.name,
            'value': self.value,
            'typeId': self.risk_field_type.id,
            'type': self.risk_field_type.name,
            'enumValues': enum_values
        }


class RiskFieldType(db.Model):
    """ 
    It models a single field type of a custom risk
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    values = db.relationship('RiskFieldEnumValue',
                             back_populates="risk_field_type")

    @staticmethod
    def get_all():
        return RiskFieldType.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class RiskFieldEnumValue(db.Model):
    """ 
    It represents a single enumeration value
    """
    id = db.Column(db.Integer, primary_key=True)
    risk_field_type_id = db.Column(db.Integer, db.ForeignKey(
        'risk_field_type.id'), nullable=False)
    risk_field_type = db.relationship("RiskFieldType", back_populates="values")
    value = db.Column(db.String(80), nullable=False)

    @staticmethod
    def get_all():
        return RiskFieldEnumValue.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
