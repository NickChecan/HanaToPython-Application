import json
from flask import Blueprint
from app.modules.Model import Model

model = Model()
controller = Blueprint('controller', "HanaToPython")


@controller.route("/api/getRegions")
def get_regions():
    return json.dumps(model.get_regions), 200, {"Content-Type": "application/json"}


@controller.route("/api/getProducts")
def get_products():
    return json.dumps(model.get_products), 200, {"Content-Type": "application/json"}


@controller.route("/api/getSalesData")
def get_sales_data():
    return json.dumps(model.get_sales_data), 200, {"Content-Type": "application/json"}

