def FindStr(Arr):

    CharArray = ["O","E","T","I","A","N","M","S","U","R","W","D","K","G","O","H","V","F",
              "Ü","L"," ","P","J","B","X","C","Y","Z","Q","CH","5","4","$","3","?","_",
              ".","-","2",":","+","*","1","6","=","/","Ç","Ð","Ö","7","8","9","0",","]

    n = len(CharArray)
    m = len(Arr)
    strArray = ""
    i = 0
    j = 0

    while i < m and j < n:
        if Arr[i] == " ":
            strArray = strArray + CharArray[j]
            j = 0
        else:
            if Arr[i] == ".":
                j = 2 * j+1
            else:
                j = 2 * j+2
        i += 1
    if j >= n:
        print("Invalid morse code at", i-1 ,"th position of the code array")

    print(strArray)


msg = ".-- .. - .... .-.- -- -.-- .-.- -... . ... - .-.- .-- .. ... .... . ... ..."

print(msg)
FindStr(msg)
