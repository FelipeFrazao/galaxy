#!/usr/bin/env bash

set -e

docker build -t grc.io/${PROJECT_DEV}/${IMAGE_NAME}:$TRAVIS_COMMIT .

echo $GCLOUD_SERVICE_KEY_DEV | base64 --decode -i > ${HOME}/gcloud-service-key.json
gcloud auth activate-service-account --key-file ${HOME}/gcloud-service-key.json

gcloud --quiet config set project $PROJECT_DEV
gcloud --quiet config set container/cluster $CLUSTER_DEV
gcloud --quiet config set compute/zone ${ZONE}

gcloud --quiet container clusters get-credentials $CLUSTER_DEV

gcloud docker -- push gcr.io/${PROJECT_DEV}/${IMAGE_NAME}

yes | gcloud beta container images add-tag gcr.io/${PROJECT_DEV}/${IMAGE_NAME}:$TRAVIS_COMMIT gcr.io/${PROJECT_DEV}/${IMAGE_NAME}:latest

kubectl -n ${K8S_NAMESPACE} set image deployment/${APP_DEPLOYMENT} ${APP_CONTAINER}=gcr.io/${PROJECT_DEV}/${IMAGE_NAME}:$TRAVIS_COMMIT
