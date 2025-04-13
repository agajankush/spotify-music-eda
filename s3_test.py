import boto3
import uuid
from pydantic import BaseModel

class S3Bucket(BaseModel):
    session: object = None # The session object
    s3_resource: object = None
    s3_client: object = None
    s3_connection: object = None # This will be either a resource conncetion or a client connection
    bucket_prefix: str = None # Name of the s3 Bucket
    choice: str# This will be either a resource or a client

    def setup_connection(self):
        if self.choice == "client":
            self.s3_connection = boto3.client('s3')
        elif self.choice == "resource":
            self.s3_connection = boto3.resource('s3')
        else:
            raise ValueError("Invalid choice. Use 'client' or 'resource'.")
        
    def create_bucket_name(self):
        # The bucket name must be unique across all AWS S3 buckets
        return ''.join([self.bucket_prefix, str(uuid.uuid4())])

    def create_bucket(self, bucket_name=None):
        self.session = boto3.session.Session()
        current_region = self.session.region_name
        # self.bucket_name = self.create_bucket_name()
        return self.s3_connection.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': current_region
            }
        )
    
    def get_bucket(self, bucket_name=None):
        # Get the bucket object
        try:
            return self.s3_connection.Bucket(bucket_name)
        except Exception as e:
            print(f"Error getting bucket: {e}")
            return None
        
    # Creating a random test file for upload
    def create_temp_file(self, size, file_name, file_content):
        random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
        with open(random_file_name, 'w') as f:
            f.write(str(file_content) * size)
        return random_file_name

    def file_upload(self, file_name, bucket_name=None, extra_args={}):
        # Upload the file to the bucket
        # Note to use ExtraArgs need to update the AWS bucket permissions on the AWS console
        # <bucket_name> -> Permissions -> Edit bucket policy & Edit Access Control List depending on the use case.
        bucket_object = self.s3_connection.Object(bucket_name, file_name)
        bucket_object.upload_file(Filename=file_name, ExtraArgs=extra_args)
        print(f"File {file_name} uploaded to bucket {bucket_name}")
        return bucket_object
    
    def file_download(self, file_name, bucket_name=None):
        # Download the file from the bucket
        bucket_object = self.s3_connection.Object(bucket_name, file_name)
        bucket_object.download_file(f'/tmp/{file_name}')
        print(f"File {file_name} downloaded from bucket {bucket_name}")
    
    def delete_file(self, file_name, bucket_name):
        # Delete the file from the bucket
        bucket_object = self.s3_connection.Object(bucket_name, file_name)
        bucket_object.delete()
        print(f"File {file_name} deleted from bucket {bucket_name}")
    
    def copy_to_bucket(self, source_bucket_name, destination_bucket_name, file_name):
        # Copy the file from one bucket to another
        copy_source = {
            'Bucket': source_bucket_name,
            'Key': file_name
        }
        destination_object = self.s3_connection.Object(destination_bucket_name, file_name)
        destination_object.copy(copy_source)
        print(f"File {file_name} copied from {source_bucket_name} to {destination_bucket_name}")

# def main():
#     print("Starting S3 test...")
#     connection = S3Bucket(choice="resource")
#     connection.setup_connection()
#     first_bucket = connection.get_bucket("firstpythonbucket0d711e2e-ea97-4f72-b6e4-8fd2d0e74865")
#     second_bucket = connection.get_bucket("secondpythonbucket354dcdfc-26ec-4fd1-b0af-4502afe18eb8")
#     second_file = connection.create_temp_file(100, "secondfile.txt", "This is a test file")
#     second_bucket_object = connection.file_upload(second_file, bucket_name=second_bucket.name, extra_args={'ACL': 'public-read'})
#     # Reading the Acl from the object
#     second_object_acl = second_bucket_object.Acl()
#     print(f"Second Object grants: {second_object_acl.grants}")
    
#     # Making the object private again
#     second_object_acl.put(ACL='private')
#     print(f"Second Object grants after permission change: {second_object_acl.grants}")
    
    

# if __name__ == "__main__":
#     main()
#     # Example usage