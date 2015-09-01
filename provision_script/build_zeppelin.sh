
cd /home/vagrant

#Install nodejs and npm manager.
sudo apt-get -y install npm


git clone https://github.com/apache/incubator-zeppelin.git
cd incubator-zeppelin
mvn clean package -Pspark-1.4 -Dhadoop.version=2.2.0 -Phadoop-2.2 -DskipTests
cd ..
rm -rf tmp/

PROFILE="/home/vagrant/.profile"
echo "export ZEPPELIN_JAVA_OPTS="\"-Dspark.jars=/mylib1.jar,/mylib2.jar -Dspark.files=/myfile1.dat,/myfile2.dat\" "
 " >>${PROFILE}
