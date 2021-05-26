# UUID Generator

### It generates a key-value pair of randomly generated UUID. Key will be a timestamp and value will be UUID.

#### e.g

```
{
    "2021-05-26 07:15:18.422153": "a85d2bf0-3697-4761-8b99-68d2a944a6e3",

    "2021-05-26 07:15:17.777608": "e4255b96-a8b1-481a-a4d0-ee0c3988c58a",

    "2021-05-26 07:15:15.827388": "17adcba1-7ace-49b2-89ae-3bdc09f556e7"
}
```

### To Test

- clone the repo
- Run `pip install -r requirements.txt`
- Start the application with `python manage.py runserver`
- using any of your API testing tool e.g Postman, Insonmia

```
GET http://127.0.0.1:8000/api/v1/generate_uuid
```