# Test Backend

The server is a very basic API which follows the [JSON API specification](http://jsonapi.org).

## Requirements

* flask
* flask_sqlalchemy
* flask_rest_jsonapi

## Test
```angular
$ chmod +x app.py
$ python app.py
```

* Then you can open http://127.0.0.1:5000/ and test

## A useful tool to test is Postman

Some examples:
* [GET] http://127.0.0.1:5000/skills
```angular2
{
    "object": [
        {
            "attribut": "java",
            "id": 2,
            "type": "Skill"
        },
        {
            "attribut": "javascript",
            "id": 3,
            "type": "Skill"
        },
        {
            "attribut": "ruby",
            "id": 4,
            "type": "Skill"
        },
        {
            "attribut": "c#",
            "id": 5,
            "type": "Skill"
        }
    ]
}
```
* [GET] http://127.0.0.1:5000/skills/2
```angular2
{
    "object": [
        {
            "attribut": "java",
            "id": 2,
            "type": "Skill"
        }
    ]
}
```
* [POST] http://127.0.0.1:5000/skills

- post body
````angular2
{
"attribut" : "c#"
}
````

```angular2
{
    "object": [
        {
            "attribut": "java",
            "id": 2,
            "type": "Skill"
        },
        {
            "attribut": "javascript",
            "id": 3,
            "type": "Skill"
        },
        {
            "attribut": "ruby",
            "id": 4,
            "type": "Skill"
        },
        {
            "attribut": "c#",
            "id": 5,
            "type": "Skill"
        },
        {
            "attribut": "c#",
            "id": 6,
            "type": "Skill"
        }
    ]
}
```

* [PUT] http://127.0.0.1:5000/skills/6

- put body:
```angular2
{
"attribut" : "communication"
}
```
```angular2
{
    "object": [
        {
            "attribut": "communication",
            "id": 6,
            "type": "Skill"
        }
    ]
}
```
* [DELETE] http://127.0.0.1:5000/skills/5

```angular2
{
    "object": [
        {
            "attribut": "java",
            "id": 2,
            "type": "Skill"
        },
        {
            "attribut": "javascript",
            "id": 3,
            "type": "Skill"
        },
        {
            "attribut": "ruby",
            "id": 4,
            "type": "Skill"
        },
        {
            "attribut": "communication",
            "id": 6,
            "type": "Skill"
        }
    ]
}
```