def q1(str, tar):
    #question 1
    #GUOLIANG LIU
    # str = "abc"
    # tar = "abcbc"
     output = 0
     index = 0
    

    while index < len(tar):
        initial = index
         

         for char in str:
             if index < len(tar) and tar[index] == char:
                index += 1

        if initial == index:
            return -1

        output += 1

    return output

#Test Case
print(shortest_way("abc", "abcbc"))  
print(shortest_way("abc", "acdbc"))  
print(shortest_way("xyz", "xzyxz"))
