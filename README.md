# NogiBlog

A website fetching blog posts by Sayaka Kakehashi from [Nogizaka46 official site](https://www.nogizaka46.com/s/n46/diary/MEMBER?ima=5608)  
including posts from [individual blog](https://www.nogizaka46.com/s/n46/diary/MEMBER/list?ima=1834&page=0&ct=48009&cd=MEMBER)
and from [4th generation relay](https://www.nogizaka46.com/s/n46/diary/MEMBER/list?ima=1604&ct=40005)

Deployed on heroku  
https://nogi-blog.herokuapp.com  
  
*Some of the photo (incluing thumbnails) cannot be shown since they are missing from the original site.

## Run the app
pre-requirement: python3.9 or above  
(Optional) Start a virtual python environment for development  
1. install required packages with  
`pip install -r requirements.txt`  

2. run scrap.py to get all the images and blogs content locally  
`python scrap.py`

3. start a local host to run the app with  
`flask run`

## Fetching Blog posts only
Code fetching blog posts can be found in the below Google Colab Notebook  
https://colab.research.google.com/drive/1s5V8WBXpH4jiwqfVTmPXktPgJaTs4YGZ?usp=sharing

The html files can be downloaded without running python on your machines.
