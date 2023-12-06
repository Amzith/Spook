# Spook
Spook is a project involved in creating tools for TTRPGs

## Handout Generation
The first tool is to create 'Handouts' which involve taking textual input and overlaying text to images, and producing the new image back. 
Just submit text into the form in the homepage, and an image will be generated.

### running locally
requires python 3.12 or later installed,

the first time run the following command to install the required python modules

`pip install --no-cache-dir -r spook/spook/requirements.txt`

then to run the django webapp run

`python spook/manage.py`

`runserver 0.0.0.0:8000`

### how to build
a new docker image is automatically created upon each push to main

then when running the image, make sure to expose the 8000 port of the container
i.e:
docker run -d -p 8080:8000 amzith/spook:latest 
