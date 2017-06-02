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

## Technology

### Main infrastructure
Project | Description | URL
--- | --- | ---
redis | key-value store (work queues) | https://redis.io/ 
mongodb | gathered info storage | https://www.mongodb.com/
rq | redis job queue | http://python-rq.org/docs/

### Linting / Vulnerability checking
Project | Description | URL
--- | --- | ---
OpenStack bandit | _Python AST-based static analyzer from OpenStack Security Group_ | https://github.com/openstack/bandit
brakeman | _A static analysis security vulnerability scanner for Ruby on Rails applications_ | https://github.com/presidentbeef/brakeman
