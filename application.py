from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Initialise the database
def init_db():
    conn = sqlite3.connect('todo.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY, 
            task TEXT NOT NULL,
            priority INTEGER DEFAULT 1
        )
    ''')
    conn.commit()
    conn.close()


init_db()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render a home page with a link to the task manager


# Route for the task manager page
@app.route('/tasks')
def tasks():
    conn = sqlite3.connect('todo.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks ORDER BY priority ASC')
    tasks = cur.fetchall()
    conn.close()
    return render_template('tasks.html', tasks=tasks)


# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    new_task = request.form.get('task')
    priority = request.form.get('priority')
    conn = sqlite3.connect('todo.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO tasks (task, priority) VALUES (?, ?)', (new_task, priority))
    conn.commit()
    conn.close()
    return redirect(url_for('tasks'))

# Route to delete a task
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    conn = sqlite3.connect('todo.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('tasks'))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False,
            host='0.0.0.0',
            port=port
    )

            