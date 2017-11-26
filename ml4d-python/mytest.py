#from sklearn.datasets import load_boston
#Boston = load_boston()
#print (Boston.data.shape)

MyTuple = (1,2,3,(4,5,6,(7,8,9)))

for Val1 in MyTuple:
    if type(Val1) == int:
        print(Val1)
    else:
        for Val2 in Val1:
            if type(Val2)==int:
                print("\t{}".format(Val2))
            else:
                for Val3 in Val2:
                    print("\t\t{}".format(Val3))
