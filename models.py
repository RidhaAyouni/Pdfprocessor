from flask_sqlalchemy import SQLAlchemy
from d import app

db = SQLAlchemy(app)

from d import db

class Reconciliation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position_date = db.Column(db.Date)
    nostro_house_collateral_account_number = db.Column(db.String(255))
    nostro_house_margin_account_number = db.Column(db.String(255))
    nostro_house_settlement_account_number = db.Column(db.String(255))
    nostro_collateral_account_number = db.Column(db.String(255))
    nostro_margin_account_number = db.Column(db.String(255))
    nostro_settlement_account_number = db.Column(db.String(255))
    calculated_house_collateral = db.Column(db.Numeric(precision=10, scale=2))
    received_house_collateral = db.Column(db.Numeric(precision=10, scale=2))
    calculated_house_margin = db.Column(db.Numeric(precision=10, scale=2))
    received_house_margin = db.Column(db.Numeric(precision=10, scale=2))
    calculated_house_settlement = db.Column(db.Numeric(precision=10, scale=2))
    received_house_settlement = db.Column(db.Numeric(precision=10, scale=2))
    calculated_collateral = db.Column(db.Numeric(precision=10, scale=2))
    received_collateral = db.Column(db.Numeric(precision=10, scale=2))
    calculated_margin = db.Column(db.Numeric(precision=10, scale=2))
    received_margin = db.Column(db.Numeric(precision=10, scale=2))
    calculated_settlement = db.Column(db.Numeric(precision=10, scale=2))
    received_settlement = db.Column(db.Numeric(precision=10, scale=2))
    status = db.Column(db.String(50))
    ecart_house_collateral = db.Column(db.Numeric(precision=10, scale=2))
    ecart_house_margin = db.Column(db.Numeric(precision=10, scale=2))
    ecart_house_settlement = db.Column(db.Numeric(precision=10, scale=2))
    ecart_collateral = db.Column(db.Numeric(precision=10, scale=2))
    ecart_margin = db.Column(db.Numeric(precision=10, scale=2))
    ecart_settlement = db.Column(db.Numeric(precision=10, scale=2))
