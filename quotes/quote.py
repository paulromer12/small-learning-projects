from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_random_quote():
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    quote = None
    
    try:
        cursor.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1")
        quote = cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()
    
    if quote is None:
        return (0, "No quotes found", "Unknown")
    return quote

@app.route('/')
def home():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)

@app.route('/quote/random')
def next_quote():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)