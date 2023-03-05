import csv
import datetime
class pizza():
  def __init__(self,description,cost):
    self.cost=cost
    self.description=description
  def get_cost(self):
    return self.cost
  def get_describe(self):
    return self.description
class Classic(pizza):
  def __init__(self):
    pizza.__init__(self,"Eşsiz Klasik Pizza",12.0)
class Margherita(pizza):
  def __init__(self):
    pizza.__init__(self,"Eşsiz Margarita Pizza",16.0)
class Turkpizza(pizza):
  def __init__(self):
    pizza.__init__(self,"Eşsiz Türk Pizzası",20.0)
class PlainPizza(pizza):
  def __init__(self):
    pizza.__init__(self,"Eşsiz Sade Pizza",24.0)
class Dominospizza(pizza):
  def __init__(self):
    pizza.__init__(self,"Eşsiz Dominos Pizza",28.0)
class Decorator(pizza):
  def __init__(self,component):
    self.component=component
  def get_cost(self):
    return self.component.get_cost() + pizza.get_cost(self)
  def get_describe(self):
    return self.component.get_describe()+" "+pizza.get_describe(self)
class Olives(Decorator):
  def __init__(self,component):
    Decorator.__init__(self,component)
    self.cost=2
    self.description="ile birlikte Zeytin Sosu deneyimi"
class Mushrooms(Decorator):
  def __init__(self,component):
    Decorator.__init__(self,component)
    self.cost=4
    self.description="ile birlikte Mantar Sosu deneyimi"
class GoatCheese(Decorator):
  def __init__(self,component):
    Decorator.__init__(self,component)
    self.cost=6
    self.description="ile birlikte Keçi Peyniri Sosu deneyimi"
class Meat(Decorator):
  def __init__(self,component):
    Decorator.__init__(self,component)
    self.cost=8
    self.description="ile birlikte Et Sosu deneyimi"
class Onions(Decorator):
  def __init__(self,component):
    Decorator.__init__(self,component)
    self.cost=10
    self.description="ile birlikte Soğan Sosu deneyimi"
class Corn(Decorator):
  def __init__(self,component):
    Decorator.__init__(self,component)
    self.cost=12
    self.description="ile birlikte Mısır Sosu deneyimi"
def main():
  menu=open("Menu.txt", "r",encoding="utf-8")
  print(menu.read())
  num1=int(input("Lütfen Seçmek İstediğiniz Pizzanın İNDEXİNİ giriniz\n"))
  assert 0<num1 and num1<6,"Geçersiz Giriş Yaptınız,doğru index değeri giriniz!"
  num2=int(input("Lütfen Seçmek İstediğiniz Sosun İNDEXİNİ giriniz\n"))
  assert 5<num2 and num2<12,"Geçersiz Giriş Yaptınız,doğru index değeri giriniz!"
  if num1==1:
      if num2==6:
        cost=Olives(Classic()).get_cost()
        describe=Olives(Classic()).get_describe()
      elif num2==7:
        cost=Mushrooms(Classic()).get_cost()
        describe=Mushrooms(Classic()).get_describe()
      elif num2==8:
        cost=GoatCheese(Classic()).get_cost()
        describe=GoatCheese(Classic()).get_describe()
      elif num2==9:
        cost=Meat(Classic()).get_cost()
        describe=Meat(Classic()).get_describe()
      elif num2==10:
        cost=Onions(Classic()).get_cost()
        describe=Onions(Classic()).get_describe()
      elif num2==11:
        cost=Corn(Classic()).get_cost()
        describe=Corn(Classic()).get_describe()
  elif num1==2:
      if num2==6:
        cost=Olives(Margherita()).get_cost()
        describe=Olives(Margherita()).get_describe()
      elif num2==7:
        cost=Mushrooms(Margherita()).get_cost()
        describe=Mushrooms(Margherita()).get_describe()
      elif num2==8:
        cost=GoatCheese(Margherita()).get_cost()
        describe=GoatCheese(Margherita()).get_describe()
      elif num2==9:
        cost=Meat(Margherita()).get_cost()
        describe=Meat(Margherita()).get_describe()
      elif num2==10:
        cost=Onions(Margherita()).get_cost()
        describe=Onions(Margherita()).get_describe()
      elif num2==11:
        cost=Corn(Margherita()).get_cost()
        describe=Corn(Margherita()).get_describe()
  elif num1==3:
      if num2==6:
        cost=Olives(Turkpizza()).get_cost()
        describe=Olives(Turkpizza()).get_describe()
      elif num2==7:
        cost=Mushrooms(Turkpizza()).get_cost()
        describe=Mushrooms(Turkpizza()).get_describe()
      elif num2==8:
        cost=GoatCheese(Turkpizza()).get_cost()
        describe=GoatCheese(Turkpizza()).get_describe()
      elif num2==9:
        cost=Meat(Turkpizza()).get_cost()
        describe=Meat(Turkpizza()).get_describe()
      elif num2==10:
        cost=Onions(Turkpizza()).get_cost()
        describe=Onions(Turkpizza()).get_describe()
      elif num2==11:
        cost=Corn(Turkpizza()).get_cost()
        describe=Corn(Turkpizza()).get_describe()
  elif num1==4:
      if num2==6:
        cost=Olives(PlainPizza()).get_cost()
        describe=Olives(PlainPizza()).get_describe()
      elif num2==7:
        cost=Mushrooms(PlainPizza()).get_cost()
        describe=Mushrooms(PlainPizza()).get_describe()
      elif num2==8:
        cost=GoatCheese(PlainPizza()).get_cost()
        describe=GoatCheese(PlainPizza()).get_describe()
      elif num2==9:
        cost=Meat(PlainPizza()).get_cost()
        describe=Meat(PlainPizza()).get_describe()
      elif num2==10:
        cost=Onions(PlainPizza()).get_cost()
        describe=Onions(PlainPizza()).get_describe()
      elif num2==11:
        cost=Corn(PlainPizza()).get_cost()
        describe=Corn(PlainPizza()).get_describe()
  elif num1==5:
      if num2==6:
        cost=Olives(Dominospizza()).get_cost()
        describe=Olives(Dominospizza()).get_describe()
      elif num2==7:
        cost=Mushrooms(Dominospizza()).get_cost()
        describe=Mushrooms(Dominospizza()).get_describe()
      elif num2==8:
        cost=GoatCheese(Dominospizza()).get_cost()
        describe=GoatCheese(Dominospizza()).get_describe()
      elif num2==9:
        cost=Meat(Dominospizza()).get_cost()
        describe=Meat(Dominospizza()).get_describe()
      elif num2==10:
        cost=Onions(Dominospizza()).get_cost()
        describe=Onions(Dominospizza()).get_describe()
      elif num2==11:
        cost=Corn(Dominospizza()).get_cost()
        describe=Corn(Dominospizza()).get_describe()
  print(f"Alınmış Olan Sipariş:\n{describe}\nToplam Tutar:\n{cost}")
  name=input("Lütfen Kullanıcı Adınızı Yazınız\n")
  id=input("Lütfen 11 Haneli TC Kimlik numaranızı Yazınız:\n")
  assert len(id)==11 and int(id),"Lütfen TC Kimlik Numaranızı Sadece rakamlardan oluşan 11 hane olarak giriniz"
  credit_card_number=input("Lütfen Kredi Kartınınızın Numarasını Giriniz\n")
  assert len(credit_card_number)==16 and int(credit_card_number),"Lütfen Kredi Kartı Numaranızı sadece rakamlardan oluşacak şekilde 16 hane olarak giriniz!"
  credit_card_password=input("Lütfen Kredi Kartınızın Şifresini Giriniz\n")
  assert ((len(credit_card_password)==4 or len(credit_card_password)==5) and int(credit_card_password)),"Lütfen Kredi Kartı Şifrenizi sadece rakamlardan oluşacak şekilde 4 veya 5 hane olarak giriniz!"
  order_info=input("Sipariş açıklamanız varsa giriniz\n")
  now=datetime.datetime.now()
  headerList=["Pizza","Pizza Sauce","Name,Identity Number","Credit Cart Number","Credit Cart Password","Order Info,Date and Time"]
  with open("Orders_Database.csv", "a", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([num1,num2,name,id,credit_card_number,credit_card_password,order_info,now])
    file.close
  database=open("Orders_Database.csv")
  print(database.read())
if __name__=="__main__":
  main()
