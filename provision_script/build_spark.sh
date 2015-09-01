
sudo apt-get update

#Install scala
sudo apt-get -y install scala

#Install maven .
sudo apt-get -y build-dep  maven maven2
sudo apt-get -y install git build-essential python-protobuf protobuf-compiler
sudo apt-get -y install ant unp python2.7 openjdk-7-jre-headless
sudo apt-get -y purge maven maven2
sudo apt-get -y install gdebi
wget http://ppa.launchpad.net/natecarlson/maven3/ubuntu/pool/main/m/maven3/maven3_3.2.1-0~ppa1_all.deb
sudo gdebi -n maven3_3.2.1-0~ppa1_all.deb
sudo ln -s /usr/share/maven3/bin/mvn /usr/bin/mvn
sudo rm maven3_3.2.1-0~ppa1_all.deb


#Download Spark.
wget http://mirror.apache-kr.org/spark/spark-1.4.1/spark-1.4.1.tgz
tar -xvf spark-1.4.1.tgz
rm spark-1.4.1.tgz
mv spark-1.4.1 spark

#Build Spark.
cd spark

export MAVEN_OPTS="-Xmx2g -XX:MaxPermSize=512M -XX:ReservedCodeCacheSize=512m"
./build/mvn -Pyarn -Phadoop-2.4 -Dhadoop.version=2.4.0 -Phive -Phive-thriftserver -DskipTests clean package

PROFILE="/home/vagrant/.profile"
echo "export PATH=""${PATH}:/home/vagrant/spark/bin"" " >>${PROFILE}
