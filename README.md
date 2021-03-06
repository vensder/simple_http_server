[![Build Status](https://travis-ci.org/vensder/simple_http_server.svg?branch=master)](https://travis-ci.org/vensder/simple_http_server)

# Simple Python http server in a Docker container

Simple Python 2.7 HTTP server with GET, POST and HEAD requests handling in a Docker container.

Jenkins can automatically detect and build newly created tags in a git repo.

Configure in Advanced settings of Jenkins Job: 
Click on the Advanced button below the repository URL and enter this paremeters:

Refspec:
``+refs/tags/*:refs/remotes/origin/tags/*``


Branches to build -> Branch Specifier:
``*/tags/*``


Include this commands in Jenkins Job script:
```sh
TAG=${GIT_BRANCH##origin/tags/}

docker build -t simple_http_server:$TAG .

tag=$TAG docker-compose up -d
```
Don't forget to enable SCM polling.


