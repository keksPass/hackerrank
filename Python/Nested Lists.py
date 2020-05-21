if __name__ == '__main__':
    students={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students[name]=score
    scores = students.values()
    second=sorted(list(set(scores)))[1] 
    second_lowest=[] 
    for key,value in students.items():  
        if value==second:
            second_lowest.append(key) 
            second_lowest.sort() 
    for name in second_lowest: 
        print (name) 
