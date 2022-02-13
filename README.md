## Cloning a repository
`git clone https://github.com/Stovart397/Docker-python-flask-web-calendar-app.git`

## Build Container
`docker build --tag python-docker .`
## RUN Container
`docker run --publish 8000:5000 python-docker`
or
`docker run -d -p YOUT_HOT_IP_XXX.XXX.XXX.XXX:8000:5000 python-docker`
## View Container
`docker ps -a`

`curl -i OUT_HOT_IP_XXX.XXX.XXX.XXX:8000:5000 `  

## PUSH Docker IMAGE in DockerHUB
1. Docker push using that same tag
2. Example:

- `docker tag your-tag yourRepositoryName/yourImageName:tag`
- `docker push yourRepositoryName/yourImageName:tag`

## DONE!
![This is an image](https://github.com/Stovart397/Docker-python-flask-web-calendar-app/blob/main/screen.png)
### URL myIMAGE on DOCKER-HUB  
### docker url












