## CPoint5 - Assignment
I build the APIs assignment by using Django Rest Framework. In this project, I create two method in single  view which is GET and POST method. 

### Database
I created the model **Glocery**  with following fields.
1. ID :- Unique number for product which is automatically updated.
2. Name :- Name of the product
3. Quantity :- Quantity of the product
4. Price :- Cost of the product
### How to run the code
- Code to run project - `python manage.py runserver`
### Process 
- Run the project by using above command.
- Login to [admin panel](http://127.0.0.1:8000/admin/).
- User credentials
	- username : kinga
	- password : Test@123
- Their use can add data manually.
- Go to [API](http://127.0.0.1:8000/glocery/)
- First component is GET method. click on "GET"  button to get the data.
- Second component is POST method. 
- Select the json method.
- Add data in below field 
	- ``` 
		{"name" : "Bus cover",
		"quantity" : 3,
		"price" : "34.3"}
- Click on POST button to add the data.