## Demo
Basis Django Project with MariaDb and Redis(Cache), Mongo, DRF

#### Install Docker
https://docs.docker.com/docker-for-mac/install/

#### Clone Repository
git clone https://github.com/PoloPing/development_demo.git

#### Run Repository
docker-compose -f dev_backend.yaml up -d

Notify: The first time starts MariaDb will be slow, so please wait about 10s

#### Check URL
connect to http://localhost:8000/ and you will see

![Alt text](pictures/index.png?raw=true)

#### Test Command
pytest -s --cov-report term --cov=./ --cov-config=.coveragerc

