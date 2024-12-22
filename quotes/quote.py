from flask import Flask, render_template, send_file
from typing import Tuple
import sqlite3
import logging
from io import BytesIO

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_random_quote() -> Tuple[str, str, int, bool]:
    """
    Retrieves a random quote with image status
    Returns: Tuple of (quote, author, id, has_image)
    """
    try:
        with sqlite3.connect('quotes.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT quote, author, id, 
                       CASE WHEN image IS NOT NULL AND image != '' 
                            THEN 1 ELSE 0 END as has_image
                FROM quotes 
                ORDER BY RANDOM() 
                LIMIT 1
            """)
            quote = cursor.fetchone()
            if quote is not None:
                return quote
            return ("No quotes found", "Unknown", None, False)
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        return ("Database error occurred", "System", None, False)

@app.route('/')
def home():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)

@app.route('/image/<int:quote_id>')
def get_image(quote_id):
    try:
        with sqlite3.connect('quotes.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT image FROM quotes WHERE id = ?', (quote_id,))
            image_data = cursor.fetchone()
            if image_data and image_data[0]:
                return send_file(
                    BytesIO(image_data[0]),
                    mimetype='image/jpeg'
                )
        return "No image found", 404
    except Exception as e:
        logger.error(f"Error serving image: {e}")
        return "Error loading image", 500

if __name__ == '__main__':
    app.run(debug=True)