[![Build Status](https://travis-ci.com/ChristianPlesca/Milestone-Project4.svg?branch=master)](https://travis-ci.com/ChristianPlesca/Milestone-Project4)

Live Version of the Website can be found [Here](http://www.treasure-huntuk.co.uk/products/) 

# Treasure Hunt 
Treasure Hunt is an E-commerce/Auction application helping users purchase and bid for various historical artifacts they share an interest in. The app lets you create an account log in, view product details such as description, dimensions, multiple images, etc. The app also has a bid system where users can bid for an item at a higher price or the can choose to buy the product at the initial asking price. There is also a profile page where you can update and your profile image, description, and so on. And the last there a contact form that will enable you to send an email to the site owner. 

# UX
### Strategy 
Treasure Hunt was designed primarily for users interested in Antique artifacts. The site helps users find interesting artifacts where they can find some more info about each artifact bid on it or purchase. 
I implemented ease access through the website where users can effectively find what exactly they are looking for.
There were no templates used for this project, I designed everything myself, he the following link shows the initial mockups for the Wintersun Website using pen and paper(https://github.com/ChristianPlesca/Milestone-Project4/tree/master/wireframes). The site was designed with mobile-first approach in mind so it is responsive across all platforms. Overall the application was designed to be easy to use very clear and easy to navigate.  

### User Stories 
As for the goal of this application, users must be able to:
* Log In/Log Out/Reset Password/Create Account
* See a list of products
* Search for a product
* Purchase a product only if the Bid price for that product is lower than the asking price
* Bid for a product only if they bid higher 
* See product details such as description, where it comes from, who belonged to etc...
* Update their profiles with content

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
*  The application was constantly tested during development using Opera GX dev tools. I used this to resize the browser to check the new code was working, breakpoints, and different mobile/tablet screen sizes.
* After deployment, I've tested the website on multiple browsers such as Mozilla(FireFox), Opera, Chrome, Microsoft Edge, Safari.
* Used https://jshint.com for testing Javascript files - No major issues were found
* Used [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly?utm_source=support.google.com/webmasters/&utm_medium=referral&utm_campaign=%206352293) - received this page is easy to use on a mobile device
* Used HTML and CSS validator [NuHTMLChecker](https://validator.w3.org/nu/#textarea) and [W3C-CSS](https://jigsaw.w3.org/css-validator/validator) - No major issues found
* All automated testing was done using Travis-CI. There is automated testing done for all apps with views, models, and forms except the bid app which i didn't implement the automated tests for but it will be implemented soon. However the Bid app was tested manually.
* You can find the automated tests in the tests.py file.

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
* Used AWS S3 for hosting static files and media 
* Finally linked my Heroku app to my Github enabled the automatic deploys and deployed the project


## Credits
Recived great help from [Stackoverflow](https://stackoverflow.com/)

### Media 
* Images were taken from [Google](https://www.google.com/)

Website for educational purposes only.