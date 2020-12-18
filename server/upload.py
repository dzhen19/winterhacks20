"""
Handles signing uploads correctly
"""
from flask import Blueprint, request, jsonify
import boto3
import mimetypes

Upload = Blueprint('upload', __name__)


# this really shouldn't be commited to source control,
# but hopefully you won't abuse this!
# these credentials give read/write access to the kapwing-uploads bucket on s3
AWS_KEY = 'AKIA2YJ3H2ADCIYPLSDD'
AWS_SECRET = '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'
AWS_BUCKET = 'kapwing-uploads'

session = boto3.Session(aws_access_key_id=AWS_KEY,
                        aws_secret_access_key=AWS_SECRET)
s3 = session.client('s3')


@Upload.route("/upload/sign")
def sign_upload():
  object_name = request.args['objectName']
  content_type = mimetypes.guess_type(object_name)[0]

  # create signed url for PUT request
  signed_url = s3.generate_presigned_url(
      'put_object', {'Bucket': AWS_BUCKET,
                     'Key': object_name, 'ContentType': content_type, 'ACL': 'public-read'}, ExpiresIn=3600, HttpMethod='PUT')

  # reference URL for uploaded object
  url = 'https://kapwing-uploads.s3.amazonaws.com/' + object_name

  print(url)
  return jsonify({'signedUrl': signed_url, 'url': url, 'key': object_name})


# uploads a file to s3 from flask server
# returns the url to the uploaded file
def upload_file(file_path):
  # get the file name from the file path
  key = file_path.rsplit('/', 1)[-1]
  content_type = mimetypes.guess_type(key)[0]

  s3 = session.resource('s3')
  s3.meta.client.upload_file(
      Filename=file_path, Bucket=AWS_BUCKET, Key=key, ExtraArgs={'ContentType': content_type, 'ACL': "public-read"})

  url = 'https://kapwing-uploads.s3.amazonaws.com/' + key
  return url
