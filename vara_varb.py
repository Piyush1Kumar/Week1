if isinstance(varA,basestring) or isinstance(varB,basestring):
    print("string involved")
if len(str(varA))>len(str(varB)):
    print("bigger")
elif len(str(varA))==len(str(varB)):
    print("equal")
else:
    print("smaller")