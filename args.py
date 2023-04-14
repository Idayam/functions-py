def mycountry(country="Rwanda"):
    print(f"Hello from{counrty}")


def greet(*names):
    for name in names:
        print(f"Hello{name}")


def studentattributes(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

def concatenate_args(*names):
    answer = ""
    for name in names"
    answer+=name
return answer


def concatenate_kwargs(**integers):
    answer = ""
    for key,value in integers.items():
        answer+= " "+value
return answer