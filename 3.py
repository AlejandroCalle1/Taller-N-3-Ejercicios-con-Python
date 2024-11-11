def eliminar(str1, str2):
    out1 = ""
    out2 = ""
    for palabra in str1:
        if palabra not in str2:
            out1 = palabra + out1
            

    for palabra in str2:
        if palabra not in str1:
            out2 = palabra + out2

    return out1, out2
str1 = "abcdef"
str2 = "defghi"
out1, out2 = eliminar(str1, str2)

print(out1)  
print(out2)  