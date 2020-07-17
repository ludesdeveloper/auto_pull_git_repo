import subprocess
import os

#git pull using popen
p = subprocess.Popen(["git", "pull", "https://username:password@git.url.co.id/user/app.git", "master"], stdout=subprocess.PIPE)
#read output
out = p.stdout.read()
print (out)
#creating docker in server if repo is updated
if 'Updating' in str(out):
    #stop all container running
    os.system("docker stop $(docker ps -a)")
    #delete all container
    p = os.popen("docker system prune", "w")
    p.write("y\n")
    #delete images
    os.system("docker rmi app")
    #building new images base on new file after pulling from repo
    os.system("docker build -t app .")
    #running docker
    os.system("docker run -d -p 5001:5002 app")
    os.system("docker run -d -p 5002:5002 app")
    os.system("docker run -d -p 5003:5002 app")
    os.system("docker run -d -p 5004:5002 app")
    os.system("docker run -d -p 5005:5002 app")
    os.system("docker run -d -p 5006:5002 app")
    os.system("docker run -d -p 5007:5002 app")
    os.system("docker run -d -p 5008:5002 app")
    os.system("docker run -d -p 5009:5002 app")
    os.system("docker run -d -p 5010:5002 app")

