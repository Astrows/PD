
def izvadit_izmaksu_izklajot(cena, linoleja_platums, platums, garums, izklajosanas_veids):
  # rest of your code...

  while True:
    if izklajosanas_veids == "Garuma": 
      garuma_input = int(input("Garumā: "))
      izmaksas = (cena + linoleja_platums + platums + garums)
      print("izklājot garumā:")
      print(izmaksas)
      break  # Exit the loop if valid input is provided

    elif izklajosanas_veids == "Platuma":
      platuma_input = int(input("Platumā: "))
      izmaksas = (cena + linoleja_platums + garums + platuma_input)
      print("izklājot platumā:")
      print(izmaksas)
      break  # Exit the loop if valid input is provided
    else:
      print("Nepareizs izklāšanas veids")
      break  # Exit the loop if valid input is provided
# Define variables with correct names
cena = 2.25
linoleja_platums = 2.0
platums = 5.25
garums = 6.0

# Call the function with the correct variable names
izklajosanas_veids = "Garuma"
izvadit_izmaksu_izklajot(cena, linoleja_platums, platums, garums, izklajosanas_veids)


izklajosanas_veids = "Platuma"
izvadit_izmaksu_izklajot(cena, linoleja_platums, platums, garums, izklajosanas_veids)
