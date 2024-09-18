from flask import Flask, request, redirect, jsonify
from url_shortener import URLShortener

app = Flask(__name__)
shortener = URLShortener()

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json.get('url')
    if not original_url:
        return jsonify({'error': 'URL is required'}), 400

    short_url = shortener.shorten_url(original_url)
    return jsonify({'short_url': request.host_url + short_url}), 201

@app.route('/<short_code>', methods=['GET'])
def redirect_url(short_code):
    original_url = shortener.expand_url(short_code)
    if original_url:
        return redirect(original_url)
    return jsonify({'error': 'Short URL not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
