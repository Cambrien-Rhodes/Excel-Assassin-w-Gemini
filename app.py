from flask import Flask, render_template, request, send_file
from engine import run_assassin, generate_reorder_summary
import pandas as pd


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/assassinate', methods=['POST'])
def assassinate():
    uploaded_file = request.files  ["uploaded_file"]
    threshold = request.form.get("threshold", type=int) 

    if not uploaded_file:
     return "No file uploaded", 400
    
    processed_file, df_flagged = run_assassin(uploaded_file, threshold)

    ai_summary = generate_reorder_summary(df_flagged)

    table_html = df_flagged.to_html(classes='table', index=False)

    return render_template('results.html', table=table_html, summary=ai_summary)

if __name__ == '__main__':
    app.run(debug=True)
