from flask import Blueprint, render_template
import pandas as pd
main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    df = pd.read_csv('data/vagas.csv')
    summary = df.groupby('departamento').size().to_dict()
    return render_template('dashboard.html', summary=summary)