curl +json data = file

iam = identity access management
aws keys = secret keys and access keys
permission ec2
your_man username

class 2

created iam
logged in 
cloned splunk setup after creating ssh keys
installed java apt install default-jre
or sudo apt update
sudo apt install fontconfig openjdk-17-jre
java -version
openjdk version "17.0.8" 2023-07-18
OpenJDK Runtime Environment (build 17.0.8+7-Debian-1deb12u1)
OpenJDK 64-Bit Server VM (build 17.0.8+7-Debian-1deb12u1, mixed mode, sharing)

installed maven apt install maven

installed jenkins
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins

installed 

tools cloud monitoring cost optimization automation securit leadership performance

ci = whenever code is pushed into github cicd is triggered(webhook) , continuous deployment = itll be deployed, trigger new change immediately when u push code

cd = whenever there is a new version tat is automatically deployed onto various servers is cd

xmatters

code - git - github - unit test - sonarqube - build - artifact - docker - k8 - monitoring - loop

ever thing / tools have master and slave relation
master(tool) tells slave server to do x y z

kvm + qemu https://www.tecmint.com/install-qemu-kvm-ubuntu-create-virtual-machines/

jenkins : pipeline -> agent -> stages -> stage -> steps -> script
pipeline webhook is for jenkins



k8
k8 is not tool it is pro
done by google

hands on installation
kubectl run web-server --image=nginx or write manifest
that will go to api that will go to kubelet of a node/minion and the node will create a contaioner and kubelet will again tell back api and api will communicate to scheduler later the api will again upate in etcd , and then it will come back to api again controller will amintain, it uses ipc inside and tcp/ip for inter node
api is the main
scheduler will act on request only



kubeadm init