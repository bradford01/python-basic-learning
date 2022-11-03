# scope: what variable do i have access to
a = 1
def parent():
    def confusion():
        return a
    return confusion()


print(parent())
print(a)




#1 - start with local
#2 - Parent local?
#3 - Global
#4 - built in python




