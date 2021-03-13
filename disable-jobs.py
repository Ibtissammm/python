import jenkins
import os
server = jenkins.Jenkins('http://localhost:8080', username='admin', password='17001644')
jobs = server.get_jobs()
app_name=os.getenv('app_name')
for job in jobs :
   if job['name'].startswith("app_name")
        server.disable_job('job')


