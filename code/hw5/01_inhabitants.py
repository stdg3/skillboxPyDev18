
# import room_1 as r1
import room_1 as r1
import room_2 as r2




if __name__ == "__main__":
    print("В комнате room_1 живут:", r1.folks)
    # print("name main")
    print("В комнате room_2 живут:", r2.folks)
    ijk = "*".join(r1.folks)
    jki = r2.folks + r1.folks
    jki = "*".join(jki)
    print(type(ijk), ijk, jki)