# observability tools test

using promtail+loki+prometheus+grafana for log/metrics observation 
> docker compose up -d

## log observability
using below script to mock the log, the log files are rotated
> python print_log.py

go to http://localhost:3000/explore 

## metrics observability
using 'prometheus_client' to expose the metrics API
> python server.py

check metrics http://localhost:9090/graph in prometheus     
go to http://localhost:3000/explore/metrics/ in grafana

