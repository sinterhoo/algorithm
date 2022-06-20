def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for i in cities:
        i = i.upper()
        if not i in cache:
            if len(cache) < cacheSize:
                cache.append(i)
            else:
                if cacheSize == 0:
                    temp =0
                else:
                    cache.pop(0)
                    cache.append(i)
            answer +=5
        else:
            cache.pop(cache.index(i))
            cache.append(i)
            answer +=1
                
    return answer