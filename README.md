The main project name in the source code implementation is `dinero_project` which has one application `dinero_app`.


Refer the `requirements.txt` file to see the entire list of packages installed in this project.


In order to access the admin section of the app, go to https://dinerotest.herokuapp.com/admin/ and use the following credentials to login:

username: u34497

password: test1234


Once logged in, we can view the contents of our `Projects` model by clicking on `Projectss` under our `Dinero_app` section of the admin view. Schema implementation of the `Projects` model in the source code can be found in the `models.py` file under the `dinero_app` application. 


The `Projects` model has been exposed in the Django Admin dashboard, with ability to search and filter instances of that model based on various search and filter options. Source code reference: `dinero_app/admin.py`. We can also add/edit/delete data and instances of the `Projects` model using the Django Admin dashboard.


The `Projects` model is also exposed as an API with the help of the `Tastypie` framework. Source code reference: `dinero_app/api.py` and `dinero_project/urls.py`. The basic endpoint format for this API is `https://dinerotest.herokuapp.com/api/project/?format=json`. Search and filter options are available for Project Name, Industry, Client Name, Project Owner, Tech Stack and Team Size fields of the `Projects` model.


Examples:

<b>1) Search for project names:</b>

sample endpoint: GET https://dinerotest.herokuapp.com/api/project/?format=json&project_name=Bitcoin%20Gold

sample response:

`{"meta": {"limit": 20, "next": null, "offset": 0, "previous": null, "total_count": 1}, "objects": [{"client_name": "Bittrex", "end_date": "2017-10-26T18:00:00", "id": 6, "industry": "Cryptocurrency", "project_name": "Bitcoin Gold", "project_owner": "Unocoin", "resource_uri": "/api/project/6/", "start_date": "2017-10-26T21:31:14", "team_size": 12, "tech_stack": "Blockchain technology"}]}`



<b>2) Industry contains keyword:</b>

sample endpoint: GET https://dinerotest.herokuapp.com/api/project/?format=json&industry__contains=Crypto

sample response:

`{"meta": {"limit": 20, "next": null, "offset": 0, "previous": null, "total_count": 2}, "objects": [{"client_name": "Bittrex", "end_date": "2017-10-26T18:00:00", "id": 6, "industry": "Cryptocurrency", "project_name": "Bitcoin Gold", "project_owner": "Unocoin", "resource_uri": "/api/project/6/", "start_date": "2017-10-26T21:31:14", "team_size": 12, "tech_stack": "Blockchain technology"}, {"client_name": "Zebpay", "end_date": "2017-11-02T21:29:51", "id": 5, "industry": "Cryptocurrency", "project_name": "Virtual Currency", "project_owner": "Unocoin", "resource_uri": "/api/project/5/", "start_date": "2017-10-26T21:29:45", "team_size": 65, "tech_stack": "Python, AI, Blockchain"}]}`



<b>3) Team size greater than 20</b>

sample endpoint: GET https://dinerotest.herokuapp.com/api/project/?format=json&team_size__gt=20

sample response: 

`{"meta": {"limit": 20, "next": null, "offset": 0, "previous": null, "total_count": 2}, "objects": [{"client_name": "Zebpay", "end_date": "2017-11-02T21:29:51", "id": 5, "industry": "Cryptocurrency", "project_name": "Virtual Currency", "project_owner": "Unocoin", "resource_uri": "/api/project/5/", "start_date": "2017-10-26T21:29:45", "team_size": 65, "tech_stack": "Python, AI, Blockchain"}, {"client_name": "E-Com Biz", "end_date": "2017-10-31T21:27:12", "id": 3, "industry": "E-commerce", "project_name": "E-commerce website", "project_owner": "Dinero Software", "resource_uri": "/api/project/3/", "start_date": "2017-10-26T21:27:06", "team_size": 22, "tech_stack": "Python, Django, MySQL"}]}`



<b>4) Combination of filters:</b>

sample endpoint: GET https://dinerotest.herokuapp.com/api/project/?format=json&team_size__gt=15&project_owner=Unocoin

sample response:

`{"meta": {"limit": 20, "next": null, "offset": 0, "previous": null, "total_count": 1}, "objects": [{"client_name": "Zebpay", "end_date": "2017-11-02T21:29:51", "id": 5, "industry": "Cryptocurrency", "project_name": "Virtual Currency", "project_owner": "Unocoin", "resource_uri": "/api/project/5/", "start_date": "2017-10-26T21:29:45", "team_size": 65, "tech_stack": "Python, AI, Blockchain"}]}`

