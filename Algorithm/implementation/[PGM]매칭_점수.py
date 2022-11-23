from collections import defaultdict
import re
def solution(word, pages):
    answer = 0
    word = word.lower()

    # 1. 단어는 [a-z]+  로 문자인것들만 추출해서 검사
    # 2. 링크 점수를 알기 위해 <meta ~~ content = "cur"/> 을 키 값으로 만들어야 함
    # 3. 형태 -> dicts[cur] = {'idx':i, 'link':0, 'word':0, 'match':[], 'score':0}

    dicts = defaultdict(dict)
    
    for i in range(len(pages)):
        pages[i] = pages[i].lower()
        cur_meta = re.search('<meta property="og:url" content="https://\S+"', pages[i])[0]
        cur = cur_meta.split('https://')[1].split('"')[0]

        dicts[cur] = {'idx':i, 'link':0, 'word':0, 'match':[], 'score':0}
        
        links = re.findall('<a href="https://\S+"', pages[i])
        dicts[cur]['link'] = len(links)
        
        for link in links:
            tmp = link.split('https://')[1].split('"')[0]
            dicts[cur]['match'].append(tmp)
        
        word_match = re.finditer('[a-z]+', pages[i])
        for match in word_match:
            if match[0] == word:
                dicts[cur]['word'] += 1
        
    key_list = dicts.keys()    
    for i, key in enumerate(key_list):
        dicts[key]['score'] += dicts[key]['word']
        
        for m in dicts[key]['match']:
            if not m in key_list:
                continue
            dicts[m]['score'] += (dicts[key]['word']/dicts[key]['link'])
    
    std = list(key_list)[0]
    result = [0]
    for key in key_list:
        if dicts[std]['score'] < dicts[key]['score']:
            result = [dicts[key]['idx']]
            std = key
        elif dicts[std]['score'] == dicts[key]['score']:
            result.append(dicts[key]['idx'])
    
    return min(result)