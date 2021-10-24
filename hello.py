from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

# import os
# path = "C:\\Users\\ajayd\\Desktop\\myproject\\templates"
# for filename in os.listdir(path):
#     @app.route('/{filename}')
#     def filename(filename):
#         return render_template('{filename}')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# @app.route('/about.html')
# def about():
#    return render_template('about.html')

# @app.route('/works.html')
# def work():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contacts():
#     return render_template('contact.html')

