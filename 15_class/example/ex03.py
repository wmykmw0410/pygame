class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}: ...")


class Dog(Animal):
    def speak(self):
        print(f"{self.name}: ワン！")


class Cat(Animal):
    def speak(self):
        print(f"{self.name}: ニャー！")


class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name)    # 親(Dog -> Animal)の __init__ を呼ぶ
        self.owner = owner        # GuideDog 独自のプロパティ

    def guide(self):
        print(f"{self.name} が {self.owner} を誘導しています")


# 種類が違っても同じメソッド名で呼び出せる
animals = [Dog("シロ"), Cat("クロ"), Dog("ハチ"), Cat("ミケ")]
for a in animals:
    a.speak()

print("---")

# 継承のチェーン
guide = GuideDog("アポロ", "田中さん")
guide.speak()    # Dog の speak が使われる
guide.guide()
