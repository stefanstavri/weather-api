#!/usr/bin/bash

# End any existing process for node-red
if pgrep node-red
then
    # echo -e analog | sudo -S pkill node-red
    sudo pkill node-red
    echo -e "Killed any existing process for node-red."
fi

# Save data from api rest locally
python3 /python/apiRequest.py

# To make the JSON data more readable
python -m json.tool /python/data.json /python/finalData.json

# Upload local file into Azure Container
python3 /python/uploadAzureBlob.py

# Open node-red
echo -e "Starting Node-RED..."
sleep 3s
node-red
sleep 10s
google-chrome http://127.0.0.1:1880/
