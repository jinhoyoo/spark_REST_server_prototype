import sys
from pyspark import SparkContext

#Get arguments.
uri = sys.argv[1]
AWS_ACCESS_KEY_ID = sys.argv[2]
AWS_SECRET_ACCESS_KEY = sys.argv[3]

sc = SparkContext("local", "S3 loader")
sc._jsc.hadoopConfiguration().set("fs.s3n.awsAccessKeyId", AWS_ACCESS_KEY_ID)
sc._jsc.hadoopConfiguration().set("fs.s3n.awsSecretAccessKey", AWS_SECRET_ACCESS_KEY)

text_file = sc.textFile(uri)
words =  text_file.flatMap(lambda line: line.split(" "))
word_count = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b) 

print word_count.collect()


#counts = text_file.flatMap(lambda line: line.split(" ")) \
#             .map(lambda word: (word, 1)) \
#             .reduceByKey(lambda a, b: a + b)

#print counts
