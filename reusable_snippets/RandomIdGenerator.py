class GenerateRandomId:
    def __init__(self, length):
        self.length = length

    def Generate(self):
        import string
        import random
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(self.length))