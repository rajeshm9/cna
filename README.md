

## All Setup on tested on minikube

```
minikube start
minikube addon enable ingress
```
###### Docker build

```
docker build --network=host -f docker/Dockerfile . -t rajeshm9/cna:1.0
docker push rajeshm9/cna:1.0
```

###### Helm Configuration 
```
helm repo add bitnami https://charts.bitnami.com/bitnami
helm dependency build
helm install cnacsf
helm install cna
```

###### CNA Common Service Framework

###### Prometheus 
```
helm show values stable/prometheus
kubectl port-forward service/cnacnf-prometheus-server 8080:80
http://localhost:8080  #Prometheus GUI
curl -X POST -v http://localhost:8080/-/reload  # Reload Prometheus Config
```

###### Grafana

###### Fluentd



###### Elasticsearch
```
helm show values stable/elasticsearch
kubectl port-forward service/csf-elasticsearch-client 9200:9200
```

###### Kibana
```
helm show values stable/kibana
```