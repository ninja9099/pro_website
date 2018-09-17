from django.conf import settings
import boto3

def upload_to_s3(image, key):
    import uuid
    file_name = str(uuid.uuid4())[:12]
    complete_file_name = "%s.%s" % (file_name, key.split('.')[-1])

    s3 = boto3.client("s3", region_name=settings.REGION_NAME,
                      aws_access_key_id=settings.ACCESS_KEY_ID, aws_secret_access_key=settings.ACCESS_KEY_SECRETE)

    res = s3.put_object(Body=image, Bucket=settings.S3_BUCKET,
                        Key='images/' + complete_file_name)
    try:
        url = settings.S3_BASE_URL + '/' + \
            settings.S3_BUCKET + '/images/' + complete_file_name
    except:
        raise Exception(
            "please define the s3 bcket path for image upload to s3 or remove that field from modal")
    return url
