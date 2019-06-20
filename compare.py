
# BE SURE TO ACTIVATE VIRTUAL ENV BEFORE RUNNING SCRIPT OR IT WILL NOT WORK
# "pipenv shell" while in yaml-github directory

#  Getting users from Carta org Github and saving them to an array called gUsers

import yaml
from github import Github

# Put your Github access token within the quotes on line 11 below!
g = Github("")

print("\n" + "*"*100)
print("Your name is: " + g.get_user().name)
print("Your username is: " + g.get_user().login)

# Enter organization name within quotes below:
org = g.get_organization("")

print(org.name)

members = org.get_members()

gUsers = []
gCount = 0
for member in members:
    # print(member.login)
    gUsers.append(member.login)
    gCount += 1

# print(gUsers)
# print("Total Users: " + str(gCount))

# Getting users from terraform-github yaml file

with open("membership.yaml", 'r') as stream:
    try:
        yUsers = yaml.safe_load(stream)
        # print(yUsers)
    except yaml.YAMLError as exc:
        print(exc)

# print("*"*100)
yAdmins = yUsers.get('github_membership').get('admin')
# print(yAdmins)
# print(len(yAdmins))
yMembers = yUsers.get('github_membership').get('member')
# print(yMembers)
# print(len(yMembers))

tUsers = yAdmins + yMembers
# print("*"*100 + " All YAML USERS: " + str(len(tUsers)))
# print(tUsers)

missingUsers = []

for user in gUsers:
    if user not in tUsers:
        # print("!"*50 + " USER MISSING FROM YAML: " + user)
        missingUsers.append(user)

print("\n" + "#"*100)
print("There are " + str(len(missingUsers)) + " members in Github(" + str(len(gUsers)) + ") that are missing from YAML("+ str(len(tUsers)) + "):")
for user in missingUsers:
    print(user)
print("#"*100 + "\n")
