# URL Shortener Project

This is a Python-based URL Shortener built using Flask. The application allows users to shorten long URLs and redirect them using the generated short URL.

## Features:
- Shorten long URLs.
- Redirect to the original URL using the shortened code.
- Simple, easy-to-use API interface.

## Project Structure:
```
url_shortener/
│
├── main.py            # Main Flask application
├── url_shortener.py   # URL shortening logic
├── database.py        # In-memory database to store URLs
├── utils.py           # Utility functions (e.g., code generation)
├── requirements.txt   # List of dependencies (Flask)
```

## How to Run the Project:
1. **Clone or Download** this repository to your local machine.
2. Navigate to the project directory:
   ```
   cd E:/url_shortener
   ```
3. Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```bash
   python main.py
   ```
   The app will be running at `http://127.0.0.1:5000`.

## API Endpoints:
1. **Shorten URL**:
   - **Endpoint**: `/shorten`
   - **Method**: POST
   - **Body**:
     ```json
     {
       "url": "https://www.example.com"
     }
     ```
   - **Response**:
     ```json
     {
       "short_url": "http://127.0.0.1:5000/abc123"
     }
     ```

2. **Redirect to Original URL**:
   - **Endpoint**: `/<short_code>`
   - **Method**: GET
   - Example: `http://127.0.0.1:5000/abc123`
   - Redirects to the original URL.

## Dependencies:
- Flask (defined in `requirements.txt`)

To install the dependencies:
```bash
pip install -r requirements.txt
```

## How the URL Shortening Works:
- A short code is generated using a combination of random letters and digits.
- This short code is mapped to the original URL in an in-memory database.
- When a user visits the short URL, they are redirected to the original URL.

## Future Enhancements (Optional):
- Add persistent database support (e.g., SQLite, PostgreSQL).
- Add user authentication for tracking personal short URLs.
- Implement custom short URLs.
