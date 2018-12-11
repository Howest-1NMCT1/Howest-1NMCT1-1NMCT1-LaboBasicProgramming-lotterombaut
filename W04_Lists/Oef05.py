#oef 05

week = ["maandag","dinsdag","woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

print(week)

werkdagen = week[0:5:1]
print("Werkdag: ",werkdagen)

weekend = week[5:7:1]
print("weekend: ",weekend)

oneven = week[1:8:2]
print("Oneven weekdagen: ",oneven)

even = week[0:8:2]
print("even weekdagen: ", even)



#for day in range(week[5,7]):
 #   print(day)