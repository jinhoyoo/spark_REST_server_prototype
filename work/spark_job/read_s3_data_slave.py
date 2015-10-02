import sys
from pyspark import SparkContext


def count_word_in_text_from_s3(uri, aws_key_id, aws_access_key):
	sc = SparkContext("local", "S3 loader")
	sc._jsc.hadoopConfiguration().set("fs.s3n.awsAccessKeyId", aws_key_id)
	sc._jsc.hadoopConfiguration().set("fs.s3n.awsSecretAccessKey", aws_access_key)

	text_file = sc.textFile(uri)

	counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

	return counts.collect()
