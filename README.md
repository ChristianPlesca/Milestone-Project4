[![Build Status](https://travis-ci.com/ChristianPlesca/Milestone-Project4.svg?branch=master)](https://travis-ci.com/ChristianPlesca/Milestone-Project4)

Live Version of the Website can be found [Here](http://www.treasure-huntuk.co.uk/products/) 

# Treasure Hunt 
Treasure Hunt is an E-commerce/Auction application helping users purchase and bid for various historical artifacts they share an interest in. The app lets you create an account log in, view product details such as description, dimensions, multiple images, etc. The app also has a bid system where users can bid for an item at a higher price or the can choose to buy the product at the initial asking price. There is also a profile page where you can update and your profile image, description, and so on. And the last there a contact form that will enable you to send an email to the site owner. 

# UX
### Strategy 


### User Stories 


## Features 
### Existing Features
1. Login/Sign Up - Allows the user to create an account reset password and log in to the site
2. Product Details - Allows the user to see the description of the selected product
3. Bidding/Purchase - Allows the user to Bid a desired amount on the chosen product or purchase for the asking price
4. Contact - Allows the user to contact the site owner 
5. User profile - Allows the user to view and update its profile 


### Features Left To Implement
* Javascript polling to update the current bid price every time there is a new bid for now, I implemented a function that refreshes the browser after 15 seconds of inactivity 
* Quick bid which will allow users to bid a small amount via a button without needing to input
* Write more unit tests for the bid app 

# Technologies
1. Django | Python   
2. Javascript | Jquery | AJAX
3. CSS | Bootstrap 
4. HTML 5 
5. PostgreSQL 
6. Heroku
7. Stripe
8. AWS S3 
9. Git
10. GitHub
11. Visual Studio Code 
12. Google Fonts 
13. Font Awesome 

### Resources
* [Django Documentation](https://docs.djangoproject.com/en/3.0/)
* [Stackoverflow](https://stackoverflow.com/)
* [W3schools](https://www.w3schools.com/)
* [Google](https://www.google.com/)

## Testing

### Issues encountered
* Concurrent Updates - each time I placed a bid on a product and my friend would place another bid for the same product without refreshing the browser it would allow him to bid lower than me which potentially breaks the law of and auction, you shouldn't be allowed to bid less than the current bid price.

### Steps taken to resolve issues
* Instead of iterating through the database with a for loop in the template and then sending that value to the view I used the filter() method to get the last record in the object and then I did the comparison and all worked as expected.

## Deployment
The deployment of the website was done using Heroku, a link to the website can be found [Here](treasure-huntuk.co.uk).
To deploy to project to Heroku I used the following steps:
* Created a virtual environment using pipenv 
* Installed all the packages using pipenv install package name
* Created an app on the Heroku Platform
* Installed the package Gunicorn 
* Used echo web: gunicorn antique_shop.wsgi:application > Procfile to create the Procfile
* I set all the Config Vars in the Heroku settings from my env.py file 
* Created the requirements.txt file using pip3 freeze --local > requirements.txt
* Set Debug to False 
* Finally linked my Heroku app to my Github enabled the automatic deploys and deployed the project


## Credits
Recived great help from [Stackoverflow](https://stackoverflow.com/)

### Media 
* Images were taken from [Google](https://www.google.com/)

Website for educational purposes only.