import pyocr
from PIL import Image
from flask import (
    Flask,
    request
)

app = Flask(__name__)

html = '''
<form action="/" method="POST" enctype="multipart/form-data">
    <input type="file" name="image_file">
    <input type="submit" value="送信">
</form>
<pre>{result}</pre>
'''


@app.route('/', methods=['GET'])
def top():
    return html.format(**{'result': ''})


@app.route('/', methods=['POST'])
def ocr():
    tools = pyocr.get_available_tools()
    tool = tools[0]

    file = request.files['image_file']
    img = Image.open(file)

    text = tool.image_to_string(
        img,
        lang="jpn",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )

    # print(text)
    return html.format(**{'result': text})


if __name__ == '__main__':
    app.run()
