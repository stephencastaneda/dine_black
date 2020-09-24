# DINE.BLACK. Django Web App

## DINE.BLACK. App

Black people make up 13% of the US population, but own only 7% of businesses in the country. Although, the lack of representation can be attributed to several factors, I believe a lack of exposure in the marketplace could be a big reason! Some people have no idea so many wonderful businesses exist in their very own neighborhoods.

Dine.Black. creates a fun way for users to share their dining experiences at black owned restaurants. Users will be able to check in when they are at a certain restaurant and share their dining experience there. Other users can see the check ins at other restaurants. If they wish, they can also click on a link to be navigated to a restaurant of choice.

## Home Page

![](https://i.imgur.com/7kNdBZG.png)

## Check In Page
![](https://i.imgur.com/KNyJ87p.png)

## Favorite Restaurant Page
![](https://i.imgur.com/aZKh9zK.png)

## Google Map Naviagation Links for Each Restaurant
![](https://i.imgur.com/KBYwfbv.png)
## Steps to get the app started

1. Create a new directory in your terminal. Clone down this repository by clicking the "Clone or Download" button above, copying the SSH key, and running the following command in your terminal `git clone sshKeyGoesHere`
2. `cd dine-black` 
3. Create a virtual enviornment at the level of your project's `manage.py` file
4. Mac users, run the following:
`python -m venv dineenv`
`source ./dineenv/bin/activate`
`pip install django`
`pip freeze > requirements.txt`

Windows users, run the following:
`python -m venv dineenv`
`source ./dineenv/Scripts/activate`
`pip install django`
`pip freeze > requirements.txt`
5. Run migrations - Run the following command from `library project` folder `python manage.py makemigrations` 
Next, run `python manage.py migrate`
6. Next run `python manage.py runserver`
7. Click on `register` in the Navbar and create a new account to use the app