"""
Darkmask API
By ~ Darkmash
"""

from flask import Flask, request
from flask_cors import CORS
import logging
import zlib

app = Flask(__name__)
CORS(app)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def encode_url(url):
  return zlib.compress(url.encode()).hex()

def decode_url(url):
  return zlib.decompress(bytes.fromhex(url)).decode()

@app.route('/')
def main_func_():
  print("PING__UPTIME")
  return """
   <meta
      property="og:image"
      content="https://cdn.discordapp.com/attachments/1023460179087470663/1062001193733337158/image.png"
    />
    <meta
      name="description"
      content="An API for generating masked urls."
    />
    <meta name="keywords" content="mask , url , darkmask ,darkmash , tools , startup , coders" />
    <link
      rel="icon"
      type="image/png"
      href="https://cdn.discordapp.com/attachments/1023460179087470663/1062001193733337158/image.png"
    />
        <title>Darkmask API ~ Darkmash</title>
  ######## DARKMASH ~ DARKMASK API ~ V.1.0.0 ###################<br>
  To use the service [GET - method] ,<br>
       &nbsp /from <br>
      &nbsp &nbsp give the url as url in headers <br>       
      &nbsp &nbsp returns a masked url <br>
##############################################################
  """


@app.route('/from', methods=['GET'])
def get():
  url = request.headers.get("url")
  return "https://Darkmask.darkmash.repl.co/" + encode_url(url)


@app.route('/<url>')
def random(url):
  try:
    url = decode_url(url)
    if "https://" in url :
      return f"""
  <script>
location.href = '{url}';
</script>
      """
    else:
      return f"""
  <script>
location.href = 'https://{url}';
</script>
  """
  except:
    return "Invalid Url.."


app.run(host="0.0.0.0", port=8080)
