from flask import Flask, request, jsonify
from hanspell import spell_checker
import re

app = Flask(__name__)

# OCR 변환된 텍스트가 500자보다 긴 한글일 때
def ko_check_long(text):
    text1, text2 = text[:500], text[500:]
    text1_mod = spell_checker.check(text1.replace('\n', '')).checked
    text2_mod = spell_checker.check(text2.replace('\n', '')).checked
    text_checked = text1_mod + text2_mod
    text_checked = re.sub('[@#^*+\\/{}]', '', text_checked)
    return text_checked

# OCR 변환된 텍스트가 500자보다 짧거나 같은 한글일 때
def ko_check_short(text):
    text_checked = spell_checker.check(text.replace('\n', '')).checked
    text_checked = re.sub('[@#^*+\\/{}]', '', text_checked)
    return text_checked

# OCR 변환된 텍스트가 영어일 때
def en_check(text):
    text_split = text.split('\n')
    text_checked = ''
    for str in text_split:
        # 한 줄이 hyphen으로 끝나는 경우, 다음 줄과 띄어쓰기 하지 않고 concat
        if str[-1] == '-':
            text_checked += str
        # 한 줄이 일반 단어로 끝나는 경우, 다음 줄과 띄어쓰기 하고 concat
        else: 
            text_checked += (str + ' ')
    return text_checked

# request에  "lang", "text" 넣기
@app.route("/process", methods=['GET','POST'])
def process():
    content = request.json
    text_checked = ''
    # OCR 변환된 텍스트가 한글일 때
    if content['lang'] == 'ko':
        # 텍스트 길이가 500자보다 길 때
        if len(content['text']) > 500:
            text_checked = ko_check_long(content['text'])
        # 텍스트 길이가 500자보다 짧거나 같을 때
        else:
            text_checked = ko_check_short(content['text'])
    # OCR 변환된 텍스트가 한글이 아닐 때 (영어)
    else:
        text_checked = en_check(content['text'])
    result = {'text_checked': text_checked}
    return jsonify(result)

if __name__ == '__main__':
  app.run(host="127.0.0.1", port=5000, debug=True)