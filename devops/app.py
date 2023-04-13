#!/usr/bin/env python3
import os

import aws_cdk as cdk

from infra.r53 import R53Stack
from infra.bucket import BucketStack
from infra.cdn import CdnStack


app = cdk.App()
r53_stack = R53Stack(app, "cdk-r53-stack")
bucket_stack = BucketStack(app, "cdk-bucket-stack")
cdn_stack = CdnStack(app, "cdk-cdn-stack", hosted_zone=r53_stack.hosted_zone,agv_bucket=bucket_stack.agv_bucket)

app.synth()
