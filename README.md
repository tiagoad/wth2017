# The Machine

![Copyright CBS (image under fair-use)](http://i.imgur.com/imGHPBg.jpg)

_The Machine_ can tell if you're a good coder. 

## What is this?

Using the GitHub API, _The Machine_ can tell if you're a good coder, and why.
  
She can be used to compare job candidates, to find good coders, or to brag about your score in your twitter profile. 

* _She_ knows if you're following conventions and good practice
* _She_ finds vulnerabilities in your code
* _She_ knows if your code is being tested, and to what extent
* _She_ can tell what technology you like the most, and how you use it
* _She_ knows if commit properly
* _She_ **knows** if you use tabs or spaces
* _She_ knows everything about your code.

## Goals

- Scalability
- Reliability
- Modularity

## Install & Run

Please refer to `DEVELOPMENT.md`

## Technology

### Main infrastructure
Project | Description | URL
--- | --- | ---
RabbitMQ | Work queue / Pub-Sub | https://www.rabbitmq.com/
mongodb | Database | https://www.mongodb.com/

### Linting / Vulnerability checking
Project | Description | URL
--- | --- | ---
OpenStack bandit | _Python AST-based static analyzer from OpenStack Security Group_ | https://github.com/openstack/bandit

### Others

Project | Description | URL
--- | --- | ---
hug | Hug aims to make developing APIs as simple as possible, but no simpler. | https://github.com/timothycrosley/hug

## Architecture

### API

- RESTful
- Publishes work to the work queue
- Gets info from the database

### Work queue

- Generic topics describe data that is available
- Workers have their own queues that are subscribed to each topic (multiplexing)

### Logging

- All logs are published into a `logs` topic in RabbitMQ, and can be processed by several workers at the time.

- Some workers can receive the totality of the logs (for example, the `log.print_logs` prints all logs into the stdout) while others can share log processing for other purposes (by using a common queue bound to that topic)

### Flow

1. The API publishes a github username into the `github.start_user_process` topic

2. The `github.fetch_metadata` workers are subscribed to the `fetch_metadata` queue inside that topic. 

    1. Once work is available, the worker downloads the user meta-data, maps it into a mongoengine object and inserts/updates the data into the database.

    2. Once the metadata has been downloaded, the worker publishes into the `github.fetch_repo` topic with the repository ID

4. The `github.fetch_repos` workers are subscribed to the `fetch_repo` queue inside that topic. 

    1. Once work is available, the workers download the repositories into temporary directories.

    2. After download, the worker publishes into the `github.repo_available` topic with the repository ID
    
5. Each of the code analysis workers are subscribed their own queue inside the `github.repo_available`

    1. Once a repository has been downloaded, these workers will check if the repository language matches their analysis capabilities and runs the external tool
    
    2. After the tool has run, the report is added to the Repository mapping in the database
    
This workflow allows for an unlimited number of workers of any kind, running on any number of machines.

All the technology used (RabbitMQ and mongodb) can be replicated into an unlimited number of servers, providing infinite scalability and containment.

Analysis workers (that depend on external tools) can be run in an isolated, read-only environment to ensure security.

## TODO

- [x] Task publishing system
- [x] Database-Object mapping
- [x] `github.fetch_metadata` worker
- [x] `github.fetch_repos` worker
- [x] `analysis.bandit` worker
- [x] HTTP API
    - [x] Read user info
    - [x] Add new job
- [ ] Web interface

![](https://i.imgur.com/YzzUeZw.png)
![](https://i.imgur.com/hXXeCjR.png)
