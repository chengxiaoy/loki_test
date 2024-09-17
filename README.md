# observability tools test

using promtail+loki+prometheus+grafana for log/metrics observation 
> docker compose up -d

## log observability
using below script to mock the log, the log files are rotated
> python print_logfile.py

go to http://localhost:3000/explore 

## metrics observability
### static config
using 'prometheus_client' to expose the metrics API
> python server.py

### monitoring docker process && docker-container metrics 
check metrics http://localhost:9090/graph in prometheus     
go to http://localhost:3000/explore/metrics/ in grafana

#### caution
To enable docker engine tcp port on Mac Docker Desktop for prometheus scrape
> socat TCP-LISTEN:2375,reuseaddr,fork,bind=127.0.0.1 UNIX-CLIENT:/var/run/docker.sock


## TODO
- Authentication
- Data Persistence