# class ClassName:
#     [xxxxx].[yyyyy]() --> [yyyyy]() = attribute

# instance = örnek | пример

# attribute = özellik | свойство
# method = eylem | действие

# PS instance'tan çağrılan bir metodun self parametresi 
# instance atanan objeye bağlıdır

class MyClass:
    def __init__(self): # constructor 
        self.data = None
    # constructor = initialize (tanımlama/başlatma) object işlemi 
    # class'ı oluşturma esnasında çağrılır

    def set_data(self, value):
        self.data = value 
        # "self" class objesinin kendisini kast eder (itself)
    
    def show_data(self):
        print(self.data)
    
    # "set_data" & "show_data" funcs is attributes of this class
    # "set_data" & "show_data" fonksiyonları class'ın özelliğidir
    # aynı şekilde "self.data" class'ın attribute'u halindedir

x = MyClass() # () esnasında constructor çağrılır
y = MyClass()
# class "MyClass" objesinden x ve y örnekleri(instance) oluşturur

x.set_data("Hello") # x durumu için self = x olur
y.set_data("Pyhon") # y durumu için self = y olur

x.show_data()
y.show_data()

# set_data & show_data her bir instance için object attribute halindedir





