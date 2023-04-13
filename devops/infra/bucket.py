from aws_cdk import (
    Stack,
    aws_s3 as s3
)
from constructs import Construct

class BucketStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        agv_bucket = s3.Bucket(self, "agv-bucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            enforce_ssl=True
        )


        self.agv_bucket = agv_bucket