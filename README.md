# simple_http_server

TAG=${GIT_BRANCH##origin/tags/}

docker build -t simple_http_server:$TAG .

tag=$TAG docker-compose up -d


