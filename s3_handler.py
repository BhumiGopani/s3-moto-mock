import os
import boto3


class S3Handler:
    def __init__(self):
        self.s3_session = boto3.session.Session()
        self.s3_client = self.s3_session.client("s3")
        self.bucket = "my_bucket"
        self.file_name = "testfile.pdf"
        self.file_path = "file_to_upload/"

    def upload_s3_files(self):

        path_to_file = os.path.join(self.file_path, self.file_name)

        self.s3_client.upload_file(
            path_to_file,
            self.bucket,
            self.file_name
        )
