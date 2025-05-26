echo "Creating directories..."
sudo mkdir -p ./kaiju_data
sudo mkdir -p ./kaiju_data/in
sudo mkdir -p ./kaiju_data/config 
sudo mkdir -p ./kaiju_data/converted
sudo mkdir -p ./kaiju_data/resized
sudo mkdir -p ./kaiju_data/injected
sudo mkdir -p ./kaiju_data/chipped
echo "Directories created..."
sudo chown -R $USER:$USER ./kaiju_data
echo "Ownership of directory set."

echo "Creating address.json in kaiju_data/config..."
cat <<EOL > /home/kemack/github-projects/kaiju-detector/kaiju_data/config/address.json
{
    "full_street_address":""
}
echo "Created address.json in kaiju_data/config."
EOL
echo "Directories created and default config copied."