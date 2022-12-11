from flask import Flask, render_template, request, make_response
import os
import json

app = Flask(__name__)

def getData(blog_id):
    data = ''
    file_path = os.path.join('json', blog_id+'.json')
    try:
        with open(file_path, 'r') as openfile:
            data = json.load(openfile)
    except:
        print('cannot get the file')
    return data

@app.route('/')
def blog_index():
    files = os.listdir('json')
    files = [ x for x in files if ".json" in x ]
    files = [file.replace('.json', '') for file in files]
    files.sort(key=int)
    files.reverse()
    blogs = []
    for file in files:
        blog = getData(file)
        blogs.append(blog)
    
    data = {
        'blogs' : blogs,
    }
    return render_template("blog_list.html", data=data)

@app.route('/<blog_id>')
def blog(blog_id):
    data = getData(blog_id)
    return render_template("blog.html", data=data)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)