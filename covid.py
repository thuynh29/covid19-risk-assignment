


age = input('Please answer True or False: Are you a cigarette addict older than 75 years old? ')
chronic = input('Please answer True or False: Do you have a severe chronic disease?')
immunity = input('Please answer True or False: Is your immune system too weak?')
if age == str("True") or immunity == str("True") or  chronic == str("True"):
  print('You are in a risky group')
else:
  print ('You are not in a risky group')

