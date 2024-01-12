import boto3
from E_var import Settings
import requests 
import glob

settings=Settings()

def upload_s3():
    filenames=glob.glob(r'data/to_S3/*.csv')
    filenames=[file.replace("\\", "/") for file in filenames]
    
    for filename in filenames:
        client=boto3.client("s3",
            aws_access_key_id=settings.accesskey,
            aws_secret_access_key=settings.secretaccesskey)
        response=client.generate_presigned_post(
            Bucket =settings.bucket,
            Key=filename,
            ExpiresIn =settings.expires)

        file={'file': open(filename)}
        request=requests.post(response['url'],data=response['fields'],files=file)
        print("Status_code of S3 request",request.status_code)
        
upload_s3()
