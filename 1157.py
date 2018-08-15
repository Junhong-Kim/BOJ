from operator import itemgetter

word = input().lower()

alphabets, ret = [], []
for alphabet in word:
    if alphabet not in alphabets:
        alphabets.append(alphabet)
        ret.append({
            'alphabet': alphabet,
            'count': word.count(alphabet)
        })
ret = sorted(ret, key=itemgetter('count'), reverse=True)

try:
    if ret[0]['count'] == ret[1]['count']:
        print('?')
    else:
        print(ret[0]['alphabet'].upper())
except IndexError:
    print(ret[0]['alphabet'].upper())
