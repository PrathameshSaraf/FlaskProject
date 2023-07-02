from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Configure PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    database="flaskProject",
    user="postgres",
    password="2002"
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        college = request.form['college']



        # Insert data into PostgreSQL
        cursor = conn.cursor()
        insert_query = "INSERT INTO students (name, college) VALUES (%s, %s)"
        cursor.execute(insert_query, (name, college))
        conn.commit()
        cursor.close()

        return "Data saved successfully!"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)