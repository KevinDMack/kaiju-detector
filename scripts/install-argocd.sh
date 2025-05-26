#!/bin/bash
echo "Installing ArgoCD..."
kubectl create namespace argocd
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
helm install argocd argo/argo-cd --namespace argocd --kubeconfig /etc/rancher/k3s/k3s.yaml

echo "ArgoCD installed successfully."
echo "Verifying ArgoCD installation..."
sudo k3s kubectl get pods -n argocd

echo "Retrieve ArgoCD admin password..."
sudo k3s kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

echo "Open ArgoCD in your browser at http://localhost:8080"
sudo k3s kubectl port-forward svc/argocd-server -n argocd 8080:443

echo "Apply CRDs:
kubectl apply -k "https://github.com/argoproj/argo-cd/manifests/crds?ref=v3.0.3"

echo Install ArgoCD CLI:
curl -sLO https://github.com/argoproj/argo-workflows/releases/latest/download/argo-linux-amd64.gz
gunzip argo-linux-amd64.gz
chmod +x argo-linux-amd64
sudo mv argo-linux-amd64 /usr/local/bin/argo