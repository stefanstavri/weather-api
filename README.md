# weather-api

This is a one semester project that involves learning to handle API requested data and storing it both local and remote in *.JSON* format. For the remote part, I used Microsoft Azure Blobs to store files and the local representation was implemented using Node-RED. I have added two features to inform me if one of the parameters exceeds a threshold. The first one sends an alert via email and the second one sends the alert direclty through SMS. The implementation for both have been done in Node-RED.

## Installation

*Python*, *Requests* module and *Azure Storage Blobs* client library need to be installed

```bash
 sudo apt-get install python3

 npm install requests

 npm install azure-storage-blob
```

Also, for Node-RED I used *node-red-dashboard*, *node-red-node-twilio* and *node-red-node-email* modules.

## Usage

Go to weather-api folder and run

```bash
 # To make the file executable
 chmod +x script.sh 

 ./script.sh
```

If the connection to the API was successfully created, the value ***200*** is showed in the terminal followed by:
```bash
 File uploaded on cloud: <FILE_NAME>
```

Then, Node-RED should open together with two chrome tabs, one for the flow and the second one with a little UI for analyzing the data.

## Links
API Documentation: [Open-Meteo](https://open-meteo.com/)  
Cloud Stored Data: [Azure Storage Blob](https://weatherapiproject.blob.core.windows.net/datacontainer/finalData.json)
