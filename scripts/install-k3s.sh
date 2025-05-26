#!/bin/bash
echo "Installing k3s..."
curl -sfL https://get.k3s.io | sh -
echo "K3s installed successfully."

echo "Starting k3s service..."
echo "Updating permissions for k3s..."
sudo chmod 644 /etc/rancher/k3s/k3s.yaml
echo "K3s service started and permissions updated."