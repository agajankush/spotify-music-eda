from pydantic import BaseModel, Field
import boto3

class Spotify(BaseModel):
    path: str = Field(
        ...,
        description="Path to the Spotify data file.",
    )
    session: object= None
    s3_connection: object=None
    choice: str
    
    def setup_connection(self):
        if self.choice == "client":
            self.s3_connection = boto3.client("s3")
        elif self.choice == "resource":
            self.s3_connection = boto3.resource("s3")
        else:
            raise ValueError("Invalid Choice. Use 'client' or 'resource'")
    
    def get_bucket(self, bucket_name=None):
        try:
            return self.s3_connection.Bucket(bucket_name)
        except Exception as e:
            # self.create_bucket()
            print(f"Error gettin Bucket {e}")
            return None
    
    def file_upload(self, file_name, bucket_name):
        bucket_object = self.s3_connection.Object(bucket_name, file_name)
        bucket_object.upload_file(Filename=file_name)
        print(f"File {file_name} uploaded to the bucket {bucket_name}")

def main():
    session = Spotify("resource")
    session.setup_connection()