# Flask Simple Web API

Contoh sederhana membuat REST API menggunakan framework Flask.

Sebelum menjalankan, lakukan instalasi dependency terlebih dahulu menggunakan file `requirements.txt`.

Untuk melakukan setting otomatis, dapat langsung menjalankan file `env.fish` untuk fish atau `env.sh` untuk bash.

Aplikasi ini menerapkan `multiprocessing` pada bagian pencariannya.

## Set environment

```sh
set -x FLASK_APP app.py
set -x FLASK_ENV production
```

atau
```sh
source env.fish
```

## Install dependency

```sh
pip install -r requirements.txt
```

## Run the app

```sh
flask run
```

## Run unittest

```sh
python -m unittest -v test_*
```

## Routes

| Endpoint          | Method | Rule                       |
| ----------------- | ------ | -------------------------- |
| hello             | GET    | /                          |
| api_manga_all     | GET    | /api/v1/manga              |
| api_manga_destroy | DELETE | /api/v1/manga/destroy/{id} |
| api_manga_find    | GET    | /api/v1/manga/find/{id}    |
| api_manga_post    | POST   | /api/v1/manga/add          |
| static            | GET    | /static/{filename}         |

# Example

## Get list

### Request

`GET /api/v1/manga`

```curl
curl -i -H "Accept: application/json" http://localhost:5000/api/v1/manga
```

### Response

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 456
    Server: Werkzeug/2.0.3 Python/3.10.3
    Date: Fri, 25 Mar 2022 16:33:08 GMT

    {"data":[{"id":1,"myanimelist":{"popularity":32,"ranked":49,"rating":8.7,"studio":"MAPPA"},"name":"Jujutsu Kaisen"},{"id":2,"myanimelist":{"popularity":357,"ranked":298,"rating":8.22,"studio":"A-1 Pictures"},"name":"86"},{"id":3,"myanimelist":{"popularity":519,"ranked":694,"rating":7.91,"studio":"Bones"},"name":"Vanitas no Karte"},{"id":4,"myanimelist":{"popularity":265,"ranked":974,"rating":7.75,"studio":"CloverWorks"},"name":"Wonder Egg Priority"}]}

## Create a new thing

`POST /api/v1/manga/add`

### Request

```curl
curl -i -H "Content-Type: application/json" -d '{"id":5,"name":"Chainsaw Man","myanimelist":{"rating":0,"ranked":0,"popularity":0,"studi
o":"MAPPA"}}' http://localhost:5000/api/v1/manga/add
```

### Response

    HTTP/1.0 201 CREATED
    Content-Type: application/json
    Content-Length: 101
    Server: Werkzeug/2.0.3 Python/3.10.3
    Date: Fri, 25 Mar 2022 16:42:20 GMT

    {"id":5,"myanimelist":{"popularity":0,"ranked":0,"rating":0,"studio":"MAPPA"},"name":"Chainsaw Man"}

## Get a specific thing

`GET /api/v1/manga/find/{id}`

### Request

```curl
curl -i -H "Accept: application/json" http://localhost:5000/api/v1/manga/find/2
```

### Response

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 105
    Server: Werkzeug/2.0.3 Python/3.10.3
    Date: Fri, 25 Mar 2022 16:46:49 GMT

    {"id":2,"myanimelist":{"popularity":357,"ranked":298,"rating":8.22,"studio":"A-1 Pictures"},"name":"86"}
