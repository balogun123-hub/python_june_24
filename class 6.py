class Dog:

  def __init__(self,name,color,height,weight,breed,age): #init function to defined object at 
       self.name = name
       self.color = color
       self.height = height
       self.weight = weight
       self.breed = breed 
       self.age = age 

  def __str__(self):
      return self.name

  def CheckSpeed(self):
      if self.breed.Casefold() == 'retrieval':
          return f'{self.name} is a {self.breed},can run atleast 30kmph'  
      elif self.breed.casefold() == 'chihuachihua':
          return f'{self.name} is a {self.breed},can run max 15kmph'
      elif self.breed.casefold() == 'yorkshire':
          return f'{self.name} is a {self.breed},can run max 15kmph'
      elif self.breed.casefold() == 'malinois':
          return f'{self.name} is a {self.breed},can run atleast 35kmph'
      elif self.breed.casefold() == 'german sheperd':
          return f'{self.name} is a {self.breed},can run atleast 35kmph'
      elif self.breed.casefold() == 'pitbull':
          return f'{self.name} is a {self.breed},can run atleast 25kmph'
      else:
          return f'{self.name} speed can not be defined'
      
def aggressiveness(self):
    if self.breed.casefold() == 'retrieval':
        return f'{self.name} is very kind'
    elif self.breed.casefold() == 'chihuachihua':
        return f'{self.name} is born to be wicked'
    elif self.breed.casefold()  == 'yorkshier':
        return f'{self.name} is friendly'
    elif self.breed.casefold() == 'malinois':
        return f'{self.name} is very aggressive'
    elif self.breed.casefold() == 'german sheperd':
        return f'{self.name} is very aggressive'
    elif self.breed.casefold() == 'pitbull':
        return f'{self.name} is very aggressive'
    else:
        return f'{self.name} aggressiveness can not be checked'

    
      

dog1 = Dog(
       name = 'lassy',
       color = 'brown yello',
       height = '1.3',
       weight = '3',
       breed = 'basengi',
       age = '12'

             
    )
print(dog1.name)
print(dog1.color)
print(dog1.height)

   

dog2 = Dog(
       name = 'Scrophy',
       color = ' light brown',
       height = '1',
       weight = '3',
       breed = 'basengi',
       age = '12'
)


dog3 = Dog(
       name = 'persie',
       color = ' white',
       height = '2',
       weight = '4',
       breed = 'Retrieval',
       age = '7'
)


dog4 = Dog(
       name = 'Jacky',
       color = ' Black brown',
       height = '2.8',
       weight = '5',
       breed = 'German sheperd',
       age = '9'
)


 
  # write a function that print the name and age of the student 
def prof(name,age):
    print(name,age) 
# 


'''
Create a product
'''