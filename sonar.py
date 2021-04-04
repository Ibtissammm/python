from sonarqube import SonarQubeClient
#from sonarqube.api import SonarQube
import os
url = 'http://localhost:9000'
username = "admin"
password = "admin"
sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)
components = list(sonar.components.search_components(qualifiers="TRK"))
#print(components)
groupid=os.getenv("groupid")
x = groupid
for i in components :
    if i['key'].startswith(str(x)):
        print(i['key'])
        sonar.projects.delete_project(i['project'])


