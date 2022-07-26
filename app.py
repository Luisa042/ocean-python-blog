from flask import Flask, render_template
from datetime import datetime

app = Flask('henlo')

posts = [
    {
        'title': 'first!!1!',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Facere, fugiat porro culpa reiciendis labore deleniti natus expedita at maiores dignissimos molestias iure accusantium aut quo, possimus vel nemo, nam obcaecati?',
        'author': 'Nunius',
        'created': datetime(2022,7,26)
    },
    {
        'title': 'secondo!!',
        'content': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ad assumenda a deserunt nobis voluptatibus dolorem saepe facere alias rem ea earum itaque numquam explicabo, tempora tenetur quaerat magnam animi quisquam?',
        'author': 'Nunius',
        'created': datetime(2022,7,27)
    },
    {
        'title': 'troisieme!!!',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium hic eaque reiciendis quas esse, dicta expedita distinctio dolores tenetur minus eos recusandae optio suscipit culpa consequuntur? Porro voluptates repellat exercitationem!',
        'author': 'Nunius',
        'created': datetime(2022,7,28)
    },
]

@app.route('/')
def index():
    return render_template('blog.html', posts=posts)

