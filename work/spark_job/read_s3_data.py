import sys
import read_s3_data_slave as s
from pyspark import SparkContext


uri = sys.argv[1]
aws_key_id = sys.argv[2]
aws_access_key = sys.argv[3]


print s.count_word_in_text_from_s3(uri=uri, \
				  aws_key_id=aws_key_id, \
				  aws_access_key=aws_access_key )
				
