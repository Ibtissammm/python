import jenkins
import os
server = jenkins.Jenkins('http://localhost:8080', username='admin', password='17001644')
jobs = server.get_jobs()
app_name=os.getenv("app_name")
x=app_name
print(x)
for job in jobs:
    if job['name'].startswith("x"):
        print(job)
#server.disable_job('job')
#print(app_name)


