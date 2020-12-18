"""
Handles grayscaling an image
"""
from flask import Blueprint, request, jsonify
import ssl
from urllib.request import urlretrieve
from upload import upload_file
from PIL import Image
import tempfile
import shutil

# prevent any ssl issues
ssl._create_default_https_context = ssl._create_unverified_context

Grayscale = Blueprint('grayscale', __name__)

@Grayscale.route("/api/grayscale", methods=['POST'])
def make_grayscale():
  req_data = request.get_json()
  url = req_data['url']

  # get the filename and extension from url
  file_name = url.rsplit('/', 1)[-1]

  # create temporary directory, image filename, and temp image
  dirpath = tempfile.mkdtemp()
  original_image = dirpath + '/' + file_name
  grayscale_image = dirpath + '/' + 'grayscale_' + file_name

  # download image to temp_image location
  urlretrieve(url, original_image)

  # we can use Pillow to grayscale the image
  # copied from: https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
  img = Image.open(original_image).convert('L').save(grayscale_image)

  # uploaded processed image to Amazon S3
  url = upload_file(grayscale_image)

  # remove the temp directory / files
  shutil.rmtree(dirpath)

  # return the uploaded image url back to client
  return jsonify({'grayscaledImage': url})
