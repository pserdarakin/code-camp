from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return"<p>Hello, World!</p>"

@app.route('/post/tasks/<int:post_id>')
def task_post(post_id):
    return f'Post {post_id}'
