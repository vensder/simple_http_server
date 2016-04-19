# simple_http_server

Configure in Advanced settings of Jenkins Job:

Refspec:
``+refs/tags/*:refs/remotes/origin/tags/*``

Branches to build -> Branch Specifier:
``*/tags/*``


Include this commands in Jenkins Job script:
```sh
TAG=${GIT_BRANCH##origin/tags/}

docker build -t simple_http_server:$TAG .

tag=$TAG docker-compose up -d


