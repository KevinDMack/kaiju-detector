echo "Creating directories..."
sudo mkdir -p /var/kaiju_data
sudo mkdir -p /var/kaiju_data/in
sudo mkdir -p /var/kaiju_data/config
sudo mkdir -p /var/kaiju_data/converted
sudo mkdir -p /var/kaiju_data/injected
sudo mkdir -p /var/kaiju_data/out
echo "Directories created..."
sudo chown -R $USER:$USER /var/kaiju_data
echo "Ownership of directory set."
echo "Copying default config..."
bash ./scripts/copy_config.sh
echo "Copied default config."
echo "Directories created and default config copied."