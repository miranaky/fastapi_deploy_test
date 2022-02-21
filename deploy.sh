# Installing docker engine if not exists
if ! type docker > /dev/null
then
  echo "docker does not exist"
  echo "Start installing docker"
sudo yum update -y
sudo yum install -y git
sudo amazon-linux-extras install docker -y
sudo service docker start
fi

# Installing docker-compose if not exists
if ! type docker-compose > /dev/null
then
  echo "docker-compose does not exist"
  echo "Start installing docker-compose"
  sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose
fi

# To create the docker group and add your user:
groups|grep docker > /dev/null
if [ $? -eq 0 ];then
sudo usermod -a -G docker ec2-user
fi

echo "start docker-compose up: ubuntu"
sudo docker-compose -f /home/ec2-user/src/white_rabbit/docker-compose.prod.yml up --build -d