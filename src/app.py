from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# static information as metric
metrics.info('app_info', 'CNA Demo', version='1.0.3')

@app.route('/')
def main():
    return 'CNA Demo!'
    pass  # requests tracked by default

@app.route('/healthz')
@metrics.do_not_track()
def healthz():
    return "OK"
    pass