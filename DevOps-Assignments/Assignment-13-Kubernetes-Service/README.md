# Assignment 13: Kubernetes Service & Networking

## Objective
Expose a Flask application running in Kubernetes Pods using a NodePort Service.

## Implementation
- Created a Kubernetes Service manifest in k8s-manifests/web-service.yaml.
- Configured a NodePort Service named web-app-service.
- Selected Pods using the app=web-app label.
- Verified Service configuration and endpoints.
- Inspected application logs.
- Forwarded the Service to localhost:8085 for testing.

## Verification
- Both application Pods were Running and Ready.
- Service endpoints pointed to both Pods on port 5001.
- The Flask application returned a successful response using curl.

## Commands
kubectl apply -f k8s-manifests/web-service.yaml
kubectl get services
kubectl describe service web-app-service
kubectl get endpoints web-app-service
kubectl get pods --show-labels
kubectl logs <pod-name>
kubectl port-forward service/web-app-service 8085:80
curl http://localhost:8085/
