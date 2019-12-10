import os
import boto3
import logging
from dotenv import load_dotenv
from botocore.exceptions import ClientError


class Ec2(object):
    ec2client = None

    def __init__(self):

        load_dotenv()
        try:
            self.ec2client = boto3.client(
                'ec2',
                region_name=os.getenv('AWS_REGION_NAME'),
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
            )
        except ClientError as exc:
            logging.error(exc)

    def list_nodes_with_customer_id(self, customer_id):
        return self.__list_instances_with_filter([{
            'Name': 'tag:customer-id',
            'Values': [customer_id]
        }])

    def list_nodes(self):
        return self.__list_instances_with_filter()

    def __list_instances_with_filter(self, tag_filters=[]):
        return self.ec2client.describe_instances(Filters=tag_filters)
