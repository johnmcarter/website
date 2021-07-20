'''
John Carter
Created: 2021/06/30 22:02:19
Last modified: 2021/07/19 19:21:57
'''

from flask import Flask, render_template
from pathlib import Path
import json
import glob

app = Flask(__name__)
app.secret_key = '\xe8I\xe6\xeaH\xa6p\xdf\xe3.)\xc8\x97+[\xaa\xe2\\p\x13\x95U\x97E'

BLOG_FILE = Path('blogs.json').absolute()


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')  


@app.route("/food_travel", methods=["GET"])
def food():
    '''
    Return a listing of blog posts for food/travel
    '''
    with open(BLOG_FILE) as json_file:
        blogs = json.load(json_file)
        blogs = sorted(blogs.items(), key=lambda items: items[1]['id'], reverse=True)

        post_names = [blog[0] for blog in blogs]
        titles = [blog[1]['title'] for blog in blogs]
        photos = [blog[1]['photo'] for blog in blogs]
        dates = [blog[1]['date'] for blog in blogs]

        return render_template('food_travel.html',
                    post_names=post_names,
                    titles=titles,
                    dates=dates,
                    photos=photos) 


@app.route("/food_travel/<blog_title>", methods=["GET"])
def food_blogpost(blog_title):
    '''
    Get blogs from JSON file
    '''    
    with open(BLOG_FILE) as json_file:
        blogs = json.load(json_file)
        if blog_title in blogs:
            return render_template('food_travel_blog.html',
                        title=blogs[blog_title]["title"],
                        date=blogs[blog_title]["date"],
                        user=blogs[blog_title]["user"],
                        body=blogs[blog_title]["body"].split("\n"),
                        photo=blogs[blog_title]["photo"]) 


@app.route("/cars", methods=["GET"])
def cars():
    return render_template('cars.html') 


@app.route("/photos", methods=["GET"])
def photos():
    return render_template('photos.html') 


@app.route("/display_photos/<id>", methods=["GET"])
def display_photos(id):
    header = id.title().replace('_', ' ')
    path = f'static/img/{id}/'
    image_list = glob.glob(path + '*')

    return render_template('display_photos.html',
                header=header,
                path=path,
                image_list=image_list) 


if __name__ == '__main__':
    app.run(host='0.0.0.0')