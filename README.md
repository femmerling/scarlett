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
<host>/url?=<image_url>
```

And voila it will display the image
