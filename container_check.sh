#/bin/sh

DJANGO_CONTAINER_ID=`docker ps -aq --filter 'name=django'`

if [ -n "$DJANGO_CONTAINER_ID" ];
  then
    echo "django container exist"
    docker stop $DJANGO_CONTAINER_ID
    docker rm $DJANGO_CONTAINER_ID
    docker run -d -p 80:80 --name django pybo:prod
  else
    echo "django container not exist"
    docker run -d -p 80:80 --name django pybo:prod
fi
