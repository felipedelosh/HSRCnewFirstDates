"""
FelipedelosH
"""

path_data = "INPUT/" # Route of patients
data = []
separator = ";"

months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
CC = [] # Save all Documents by month
counter = 0

print("==Cargando Información==")
for i in range(1, 13):
    try:
        with open(path_data+str(i)+".csv") as f:
            data.append(f.read())
    except:
        print("la cuenta termina en:", months[counter])
        break

    counter = counter + 1


# Separate a Data
def calculateNewFirstDates(month, data):
    total_new_first_dates = 0
    all_data_month = data.split("\n")[1:-1]
    
    
    for i in all_data_month:
        _data = i.split(separator)

        _CC = str(_data[0]) + str(_data[1])

        if _CC not in CC:
            CC.append(_CC)
            total_new_first_dates = total_new_first_dates + 1


    print("Para el Mes >> ", months[month], " Total Nuevas Citas mayores de quince años >> ", total_new_first_dates)



print("==Calculando Nuevas Primeras Citas==")
counter = 0
for i in data:
    calculateNewFirstDates(counter, i)
    counter = counter + 1

