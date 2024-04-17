# kaiju-detector
The goal of this application is to show the ability to use geo-spatial imagery in a fun way from the Micrsoft Planetary Computer.  

# What does this application do?

# Why does this matter?

# Pre-requisites:
The following are required to run this application:
- vscode
- wsl 

# Running the application.
The following steps will allow you to run this application code:

## Open the Dev Container:
This code makes use of a devcontainers, so first you will need to install the pre-requisites, and then you will need to hit "F1" on your keyboard and select the option for "Rebuild without cache and reopen devcontainer."  

Once your devcontainer is open, you will see the following:

## Get your bounding box:
So everything for geospatial imagery uses the same coordinate system as we've been using for almost one thousand years.  Latitude and Longitude.  

But to make this more fun, I have a script where you can give it an address and it will build the latitude and longitude bounding box for you.  The script is found [./scripts/get_bounding_box.sh](./scripts/get_bounding_box.sh):

First update line 2 to have the address in the United States you would like to see:
```bash
address="1 Innovation Way, Harrisburg, PA 17110"
```

And then save the changes.  Then run this command from a terminal in vscode:
```bash
bash ./scripts/get_bounding_box.sh
```

And you will get output like the following:
```shell
Getting lat/long and bounding box for...
Address: 1 Innovation Way, Harrisburg, PA 17110

Exact Lat / long:
Latitude: 40.2924986
Longitude: -76.88335361791044

Bounding Box:
Min Latitude: 40.2474986
Max Latitude: 40.3374986
Min Longitude: -76.93835361791044
Max Longitude: -76.82835361791044
Generating config file for bounding box at ./data/config...
File ./data/config/bbox.json deleted.
Generated config file for bounding box at ./data/config...
```

Now, this has already generated a file the application will use to run it through our Kaiju Injector / Detector.  That file can be found at [./data/config/bbox.json](./data/config/bbox.json).

If you want to update the file at [./config/bbox.json] you can migrate it over to the data directory with this script:
```bash
bash ./scripts/copy_config.sh
```

## Build the container images:
Much like applications on orbit, or even on earth, this application makes use of docker containers for executing the different pieces.  To build the docker images, please run the following from your terminal:

```bash
bash ./scripts/build_images.sh
```
When completed, you will see the following:
TODO - Image

## Pulling Down imagery:
To pull down the imagery, you will run the following script, which will deploy the docker container to download the imagery.  

If you would like to watch the container execute, you can do so by running the following command, in a separate window:
```bash
watch -n 1 docker container ls
```
This will show you all running docker containers, and you will be able to see your container.  

Run the following command which will startup the container to get imagery.
```bash
docker run --rm -d -v /var/kaiju_data:/data kaiju/kaiju-get:0.0.1
```

To see the logs of the container, run the following, in a different terminal:
```bash
container_id=$(docker ps -aqf "ancestor=kaiju/kaiju-get:0.0.1")
watch -n 1 docker logs $container_id
```

## Converting the image to PNG:

## Running Kaiju Injection:

## What is Custom Vision?

## Build custom vision container?

## Running custom vision container?

## Running Post Processing?

## Results?