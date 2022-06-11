from collections import defaultdict

def leastInterval(tasks, n) -> int:
        key_list = defaultdict(int)
        answer = 0
        while len(tasks) != 0:
            temp = ''
            for i in tasks:
                if key_list[i] == 0:
                    answer +=1
                    key_list[i] = n
                    tasks.remove(i)
                    temp = i
                    break
            else:
                if temp != '':
                    answer +=1
            
            for key,value in key_list.items():
                if key != temp:
                    if value > 0:
                        key_list[key] -=1
                
        
        return answer

print(leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"],2))