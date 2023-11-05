from azure.storage.blob import BlobServiceClient

# Upload File to Azure Blob
storage_account_key = ""
storage_account_name = ""
connection_string = ""
container_name = ""

def uploadToBlogStorage(file_path, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

    print(f"File uploaded on cloud: {file_name}")

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

uploadToBlogStorage('PATH_TO_FILE', 'FILE_NAME')
