from google.cloud import storage


string = 'olá'

output_bucket = "pipelines-golden"

storage_source = 'teste/texto.txt'

client = storage.Client()

bucket = client.get_bucket(output_bucket)

blob = bucket.blob(storage_source)

blob.upload_from_string(string)
