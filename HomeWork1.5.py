def from_human_to_dog(dog_age, dog_name):
    human_age = dog_age * 5
    return print(f"If {dog_name} were human, his age would be: {human_age}!")


dog_age = int(input("Your dog's age: "))
dog_name = input("Your dog's name: ")

from_human_to_dog(dog_age, dog_name)
