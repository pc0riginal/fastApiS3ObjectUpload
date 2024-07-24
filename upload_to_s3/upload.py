import boto3
from dotenv import dotenv_values
config = dotenv_values(".env")
bucket = config.get('BUCKET_NAME')


# Upload object to s3
def upload(file):
    try:
        s3 = boto3.client('s3', aws_access_key_id=config.get('AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key=config.get('AWS_SECRET_ACCESS_KEY'))
        s3.upload_fileobj(file.file, bucket, file.filename)
        return "File uploaded sucessfully"
    except Exception as e:
        return e
    finally:
        print("Done")