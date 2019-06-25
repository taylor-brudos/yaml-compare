# BE SURE TO ACTIVATE VIRTUAL ENV BEFORE RUNNING SCRIPT OR IT WILL NOT WORK
# "pipenv shell" while in yaml-github directory

import yaml
from github import Github

# MEMBERS:

g = Github("")

print("\n" + "*"*100)
print("Your name is: " + g.get_user().name)
print("Your username is: " + g.get_user().login)

org = g.get_organization("")

print(org.name)

members = org.get_members()

gUsers = []
for member in members:
    # print(member.login)
    gUsers.append(member.login.lower())

# print(gUsers)
# print("Total Users: " + str(gCount))

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

tUsers = []
for admin in yAdmins:
    tUsers.append(admin.lower())
for member in yMembers:
    tUsers.append(member.lower())
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


# REPOSITORIES:

with open("repository.yaml", 'r') as stream:
    try:
        yReposRaw = yaml.safe_load(stream)
        # print(yReposRaw)
    except yaml.YAMLError as exc:
        print(exc)

yRepos = []
# print(yReposRaw)
for repoKey in yReposRaw.get('github_repository'):
    yRepos.append(yReposRaw.get('github_repository').get(repoKey).get('name').lower())

# print(yRepos)

repos = org.get_repos()

gRepos = []
for repo in repos:
    gRepos.append(repo.name.lower())

# print(gRepos)
# print(len(gRepos))

missingRepos = []
for repo in gRepos:
    if repo not in yRepos:
        missingRepos.append(repo)

print("There are " + str(len(missingRepos)) + " repos in Github(" + str(len(gRepos)) + ") that are missing from YAML("+ str(len(yRepos)) + "):")
for repo in missingRepos:
    print(repo)
print("#"*100 + "\n")
