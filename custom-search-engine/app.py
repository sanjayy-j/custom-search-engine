import os
from flask import Flask, render_template, request
from exa_py import Exa

app = Flask(__name__)
exa = Exa(os.environ.get('e54894b5-f1a9-46b8-9b70-2acd7d1a5bec'))  

@app.route('/', methods=['GET', 'POST'])
def search():
    error = None
    results = []
    query = ''
    num_results = '5'
    domain = 'https://www.instagram.com'
    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        num_results = request.form.get('num_results', '5')
        domain = request.form.get('domain', 'https://www.instagram.com').strip()
        if not query:
            error = "Please enter a search query."
        else:
            try:
                response = exa.search(
                    query,
                    num_results=int(num_results),
                    type='keyword',
                    include_domains=[domain] if domain else None,
                )
                results = response.results
            except Exception as e:
                error = f"Search API error: {str(e)}"
    return render_template('index.html', results=results, error=error, query=query, num_results=num_results, domain=domain)

if __name__ == '__main__':
    app.run(debug=True)
