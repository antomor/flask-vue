from app import db


class RiskType(db.Model):
    """ 
    It models a custom risk type
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(150), unique=False, nullable=True)
    fields = db.relationship('RiskField', backref='risk_type', lazy=True)

    def __repr__(self):
        return '<RiskType %r>' % self.name


class RiskField(db.Model):
    """ 
    It models a single field of a custom risk
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    risk_type_id = db.Column(db.Integer, db.ForeignKey(
        'risk_type.id'), nullable=False)
    value = db.Column(db.String(150), nullable=True)
    risk_field_type = db.relationship('RiskFieldType')

    def __repr__(self):
        return '<RiskField %r>' % self.name


class RiskFieldType(db.Model):
    """ 
    It models a single field type of a custom risk
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    values = db.relationship('RiskFieldEnumValue',
                             back_populates="risk_field_type")

    def __repr__(self):
        return '<RiskFieldType %r>' % self.name


class RiskFieldEnumValue(db.Model):
    """ 
    It represents a single enumeration value
    """
    id = db.Column(db.Integer, primary_key=True)
    risk_field_type_id = db.Column(db.Integer, db.ForeignKey(
        'risk_field_type.id'), nullable=False)
    risk_field_type = db.relationship("RiskFieldType", back_populates="values")
    value = db.Column(db.String(80), nullable=False)
