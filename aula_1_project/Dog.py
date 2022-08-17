from unicodedata import name


class Dog:
    def __init__(self, name, owner, birthDay, furColor, breed):
        self.name = name
        self.owner = owner
        self.birthDay = birthDay
        self.furColor = furColor
        self.breed = breed