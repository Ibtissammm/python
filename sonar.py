#from sonarqube import SonarQubeClient
from sonarqube.api import SonarQube

url = 'http://localhost:9000'
username = "admin"
password = "17001644"
sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)
components = list(sonar.components.search_components(qualifiers="TRK"))
print('components')
