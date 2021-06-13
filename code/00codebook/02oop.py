OOP

Abstraction - objenin class'ını belirleme 
    kediler için: hepsinde pati kuyruk var dolayısıyla abstract edilebilir

Inheritance / kalıtım / наследование - üst class'ın tüm method ve attribute'ların 
    alt classa'a aktarılması ya da class'ların hiyerarşisi
    kedi sınıfı hayvanlar sınıfından kalıtım almakta, hiyerarşi

Encapsulation / инкапсуляция - obje içerisinde bilgilerin tutulması
    kedi.adi: adi attribute'un değer tutması encapsule edilmiş olamsıdır

Polymorphism (poly=çok, morph=değişim) - çoklu kalıtım
    class Drone(Robot, CanFly)


class MyClass:
    var = 3 # class variable
    def __init__(self):
        self.var = 5 # yalnızca MyClass alanınında erişilebilir

a = MyClass()
a.var = 7
print(a.var) # 3 --> 7 output: 7

class variable - class'ın tüm nüshalarından erişilebilir, 
    class'ın içerisinde  methodların dışında tanımlanır

instance - class'ın nüshası, class'tan oluşturulmuş ayrı bir obje

instance variable - class nüshasının değişkeni, class'ın method'u içerisinde tanımlanır
    ve yalnızca geçerli instance'ta geçerlidir


