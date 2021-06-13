# Contex Manager __init__, __enter__, __exit__

class InOutBlock:
    def __init__(self):
        pass

    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        # raise için exc_val:
        #     exc_type - type
        #     exc_val - object
        #     exc_tb - traceback
        print("exit")

with InOutBlock() as block:
    print("working")

# output: 
#         enter
#         working
#         exit