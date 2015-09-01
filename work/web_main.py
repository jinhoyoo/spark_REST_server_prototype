import subprocess 
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class S3Data(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('uri', location='json' )
        parser.add_argument('AWS_SECRET_ACCESS_KEY', location='json' )
        parser.add_argument('AWS_ACCESS_KEY_ID', location='json' )
        args = parser.parse_args()

        cmd =[ 'spark-submit', '/home/vagrant/work/spark_job/read_s3_data.py',
            args['uri'],
            args['AWS_ACCESS_KEY_ID'],
            args['AWS_SECRET_ACCESS_KEY']
           ]

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        stdout_value = process.communicate()[0]
        output = {"output":stdout_value}
        return output, 200



api.add_resource(S3Data, '/S3Data')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
