from flask import Flask
from src.main.routers.calculator_4_route import calc_bp


app = Flask(__name__)
app.register_blueprint(calc_bp)

