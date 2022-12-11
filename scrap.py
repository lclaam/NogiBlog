import requests
import os
import json
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError

def getName(member_id):
    return {
        48009 : 'Kakehashi Sayaka',
        40005 : '4th relay',
        40006 : '5th relay',
    }.get(member_id, '')  

def getBlog(member_id):
    
    save_base = 'json'
    save_base_image = 'static/images'
    # if later wanna save more than 1 member
    # save_base = os.path.join('json', member_id)
    # os.makedirs(save_base, exist_ok=True)

    blog_link = 'https://www.nogizaka46.com/s/n46/api/json/diary?cd=MEMBER&get=B&member_id='+member_id
    result = requests.get(blog_link).json()
    blogs = result["blog"]
    

    for blog in blogs:
        
        # save the images
        soup = BeautifulSoup(blog['content'], 'html.parser')
        save_path_image = os.path.join(save_base_image, blog['pubdate'][:10].replace('/', ''))
        os.makedirs(save_path_image, exist_ok=True)

        images = soup.findAll('img')
        for image in images:
            image_url = image['src']
            image_name = image_url.split('/')[-1]
            image_path = os.path.join(save_path_image, image_name)
            # print('Saving ', image_url, ' to ', image_path)
            try:
                urllib.request.urlretrieve(image_url, image_path)
            except FileNotFoundError as err:
                print(err)   # something wrong with local path
            except HTTPError as err:
                print(err)  # something wrong with url
                print('The image cannot be found on the server: ', image_url)

            blog['content'] = blog['content'].replace(image_url, '/' + image_path)

        # save the json
        save_path = os.path.join(save_base, blog['id']+'.json')
        try:
            with open(save_path, "w", encoding='utf-8') as file:
                json.dump(blog, file)
        except:
            print('fail to save: ', blog['title'])


def getImage(member_id):
    path =  'json' #  os.path.join('json', member_id)
    files = os.listdir(path)

if __name__ == '__main__':
    member_id = 48009
    getBlog(str(member_id))