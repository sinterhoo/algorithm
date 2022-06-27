def solution(files):
    answer = []
    file_list = []
    
    for i in files:
        number_index = 0
        number_index_end = 0
        
        for k in range(len(i)):
            if i[k].isdigit() and number_index == 0:
                number_index = k
            if i[k].isdigit() == False and number_index != 0:
                number_index_end = k
                break
        if number_index_end == 0:
            temp = [i[:number_index].upper(),int(i[number_index:]),i]
        else:
            temp = [i[:number_index].upper(),int(i[number_index:number_index_end]),i]
            
            
        file_list.append(temp)
    
    file_list.sort(key=lambda x : (x[0],x[1]))
    for i in file_list:
        answer.append(i[2])
                
    return answer