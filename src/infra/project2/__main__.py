"""An AWS Python Pulumi program"""

import os
import sys

from pathlib import Path

import pulumi
from pulumi_aws import s3

# Workaround https://github.com/pulumi/pulumi/issues/7360
src_dir = os.fsdecode(Path(__file__).resolve().parent.parent.parent)
sys.path.append(src_dir)

from infra.lib import example

example.say_hello()

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
