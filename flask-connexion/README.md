```
The swagger_ui directory could not be found.
    Please install connexion with extra install: pip install connexion[swagger-ui]
    or provide the path to your local installation by passing swagger_path=<your path>

The swagger_ui directory could not be found.
    Please install connexion with extra install: pip install connexion[swagger-ui]
    or provide the path to your local installation by passing swagger_path=<your path>
```

## REST API


| Action | HTTP Verb | URL Path | Description |
|--------|-----------|----------|-------------|
| Create | POST      |/api/people   |Defines a unique URL to create a new person   |   
| Read   | GET       | /api/people  |Defines a unique URL to read a collection of people   |   
| Read   | GET       | /api/people/{person_id}  |Defines a unique URL to read a particular person by person_id   |   
| Update | PUT       | /api/people/{person_id}  |Defines a unique URL to update an existing person by person_id   |   
| Delete | DELETE    | /api/orders/{person_id}  | Defines a unique URL to delete an existing person by person_id |  

## Swagger
In the Swagger browser plugin enter the URL: `http://localhost:5000/api/swagger.json`
