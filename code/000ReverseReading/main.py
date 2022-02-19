def read_file():
    with open("data.txt", mode="r", encoding="utf-8") as data:
        with open("output.txt", mode="r+", encoding="utf-8") as output_data:
            
        for line in data:
            
                output_data.write(line)
                # input()
            input()

read_file()

data = """
asdasd\n
asda564566464\n
798989799asdasdsd\n
"""
# with open("output.txt", mode="r+", encoding="utf-8") as output_data:    
#     for line in data:
#         output_data.write(line)