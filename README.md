# Spook
Spook is a project involved in creating tools for TTRPGs

### how to build
to build the image run:
docker buildx build --platform linux/arm64 -t robingraf9/spook:arm64 .

then when running the image, make sure to expose the 8000 port of the container
i.e:
sudo docker run -d -p 40000:8000 robingraf9/spook:arm64 