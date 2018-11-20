# Item Catalog #

The project is to create a python web application build using the **flask** framework which uses a database to display items organized according to categories. The web application uses a Google+ authentication system, and users who have authenticated have the ability to perform CRUD (create, read, update, delete) functions on the items in the database. Users who have not authenticated can only views the items. 

This particular web application displays the names of the most famous recipes from each country such as 'sushi', and 'ramen' from Japan', and 'butter chicken', and 'chili chicken' from India.

### Getting Started ###

It is recommended that you use a Linux environment to deploy all the python files. 

##### Prerequisites #####

In order to compile python applications you will need a terminal program. You can download git from [here](https://git-scm.com/download/win). Install git bash on your machine. In order to work in the Linux environment you can install Vagrant from this link [here](https://www.vagrantup.com/downloads.html). Install Vagrant on your machine. The link to the flask documentation is [here](http://flask.pocoo.org/).

Download the project files and folders. The `application.py` file is the file that provides functionality for the item catalog application. The _templates_ folder contains the html templates of the web-pages that the `application.py` file accesses. The `database_setup.py` file contains all the setup configurations for the data tables that will be used to store item information. The `countryfooditems.py` file contains the initial few items that will be stored in the database. 

##### Installing #####

Please follow these steps:
1. Copy the project files and folders into a directory. 
2. Open git bash and navigate into the directory where you saved the project files.
3. Run `vagrant up` in git. When the Linux virtual machine environment is configured run 'vagrant ssh' to access the Linux environment.
4. In order to access the shared files between the Linux machine and your machine run `cd /vagrant` in your git to navigate to the shared files folder.
5. Navigate to the directory containing the `application.py` file.
6. In git run `python countryfooditems.py`. You should see the '_added food items!_' message display in git. This will create a database file called `countryfooditems.db` that will store all the items that will be added to the database. 

### Run the Application ###

The application is designed to display in the _http://localhost_ environment on port 5000. 

To see the application follow these steps:
1. Open git and navigate to the project directory.
2. Run `vagrant up` and once the Linux environment is running 'vagrant ssh' to access the Linux environment.
3. Run `cd /vagrant` and navigate to the directory containing the `application.py` file.
4. Run `python application.py` to bring up the web application.
5. In the internet browser of your choice navigate to _http://localhost:5000/_ to view the application. 
6. In order to perform the CRUD operations on the items in the database the user must sign in with their existing gmail or Google+ account. Otherwise the use can only see the items in the database. 

### Design of the Code ###

The `database_setup.py` file imports all the necessary **SQL-Alchemy** modules and then proceeds to define two main classes used in the structure of the database. The `Country` class assigns an id to each country in the database and contains its name. The `FoodItem` class has a foreign-key relationship to the country which the food item is from and contains its name and description. Each class contains serialize functions to display the contents of the database in a `JSON` format.

The `application.py` file imports all the necessary **flask** modules and then defines each route and the function associated with that route. Each function queries the database based on the route input parameters to extract the items needed and then either returns an input to another function or returns an html page with content. 

The `.html` files are html templates used by the `application.py` file to display the database items. The `.html` files are constructed with a combination of html and css.

### Built With ###

**Flask** - web framework
**SQl-Alchemy** - database framework
