# SCARLETT

Translation service to convert http served image into https. Mainly because of our good friend LINE@

## Why Scarlett?

Scarlett Johansson plays in lost in translation :D

## Requirements

* Python3.6
* Sanic
* Requests

## Installation

Install virtualenv if you haven't yet

```
$ xcode-select --install # Install Command Line Tools if not installed yet
$ sudo easy_install pip # If you haven't installed pip yet
$ sudo pip install virtualenv # If you haven't installed virtualenv yet
```

Install dependencies

```
$ virtualenv -p python3.6 env
$ source env/bin/activate
$ pip install -r requirements.txt
```

Run app

```
$ python serve.py
```

## Usage

Scarlett will download and serve any image file on the fly

use it by doing this

```
<host>/<image_url without protocol>
```

example:
`https://scarlett.prismapp.io/popoluca.com/images/some/long/scheme/someimage.jpg`

And voila it will display the image

## Environment Variables

* `SCARLETT_DEFAULT_IMG` the default image used when the url is not found

## Testing

```
$ nosetests --cover-html --cover-erase --cover-package=scarlett --cover-erase --with-xcoverage -v tests
```

