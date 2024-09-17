from prometheus_client import start_http_server, Summary
import random
import time
# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

    # currently do not support summary type metric
    # https://github.com/prometheus/client_python/issues/888
    # https: // prometheus.github.io / client_python / instrumenting / summary /
    REQUEST_TIME.observe(t)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8007)
    # Generate some requests.
    while True:
        process_request(random.random())
