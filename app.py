my_name = "Yanina Slabetska"
print("Hello and welcome " + my_name + "!")

# Another way of printing the above line without remaking a variable in a string
my_name = "Yanina Slabetska"
print("Hello and welcome {}!".format(my_name))

# Modulo
my_team = (27 % 4)
print("My team number is: " + str(my_team))
team_person_26 = (26 % 4)
team_person_28 = (28 % 4)
print("The 26th person is on team number: " + str(team_person_26))
print("The 28th person is on team number: " + str(team_person_28))

team_0 = []
team_1 = []
team_2 = []
team_3 = []

for i in range(1, 29):
    if i % 4 == 0:
        team_0.append(i)

print("Team 0 members are: ", team_0)

for i in range(1, 29):
    if i % 4 == 1:
        team_1.append(i)

print("Team 1 members are: ", team_1)

for i in range(1, 29):
    if i % 4 == 2:
        team_2.append(i)

print("Team 2 members are: ", team_2)

for i in range(1, 29):
    if i % 4 == 3:
        team_3.append(i)

print("Team 3 members are: ", team_3)

module_variable = 14 % 4
print(module_variable)
