from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
app.jinja_env.globals["abs"] = abs  # Adiciona a função abs ao Jinja

@app.route('/')
def home():
    results_df = pd.read_csv("DATA/processed/elasticity_optimal_price.csv")
    return render_template('index.html', results_df=results_df)


@app.route('/about')
def about   ():
    return render_template("about.html")


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')   

@app.route('/precos')
def precos():
    results_df = pd.read_csv("DATA/processed/elasticity_optimal_price.csv")
    return render_template('precos.html', results_df=results_df)


if __name__ == "__main__":
    print(__name__) 
    print("oi")
    app.run(debug=True)