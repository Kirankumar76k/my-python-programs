# def new(dict):
#     for x,y in dict.items():
#         yield x,y
# a={1:"hello",2:"kiran"}
# b=new(a)
# print(b)
# next(b)
# print(b)
# next(b)

def new(dict):
    for x,y in dict.items():
        yield x,y


a={1:"hello",2:"kiran"}

print(new(a)._next_())