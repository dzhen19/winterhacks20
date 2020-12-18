"""
Handles GIF making
"""
from flask import Blueprint, request, jsonify, current_app
import ssl
from urllib.request import urlretrieve
from upload import upload_file
import tempfile
import shutil
import imageio
from PIL import Image
import logging
from utils import crop_center


# prevent any ssl issues
ssl._create_default_https_context = ssl._create_unverified_context

Gif = Blueprint('gif', __name__)


@Gif.route("/api/gif", methods=['POST'])
def make_gif():
  #   current_app.logger.info()
  req_data = request.get_json()

  urls = req_data['urls']
  fps = req_data['fps']
  height = req_data['height']
  width = req_data['width']
  position = req_data['position']

  # temporary directory to house images
  dirpath = tempfile.mkdtemp()
  filenames = [url.rsplit('/', 1)[-1] for url in urls]
  original_paths = [dirpath + '/' + filename+'.png' for filename in filenames]
  # use first image's name for gif name
  gif_path = dirpath + '/' + 'gif_' + \
      filenames[0].split(
          '.')[0] + f"fps{str(fps)}_"+f"dim{width}x{height}_"+f"{position}"'.gif'

  # download image to temp_image location
  for i, path in enumerate(original_paths):
    urlretrieve(urls[i], path)
    # current_app.logger.info(path)

  frames = []
  for path in original_paths:
    im = Image.open(path)
    if (position == 'contain'):
      im.thumbnail((width, height))
      new = Image.new('RGBA', (width, height),
                      (255, 255, 255, 0))  # with alpha
      new.paste(im, (round((width - im.size[0]) / 2),
                     round((height - im.size[1]) / 2)))
      new.save(path)
    else:
      im_width, im_height = im.size
      scale_factor_w = width/im_width
      scale_factor_h = height/im_height
      scale_factor = max(scale_factor_w, scale_factor_h)

      final_size = (round(im_width*scale_factor),
                    round(im_height*scale_factor))
      im = im.resize(final_size)
      im = crop_center(im, int(height), int(width))
      im.save(path)
    frames.append(imageio.imread(path))
  imageio.mimsave(gif_path, frames, format='GIF', fps=fps)

  # uploaded processed image to Amazon S3
  url = upload_file(gif_path)
  # current_app.logger.info(url)

  return jsonify({'gifImage': url})
