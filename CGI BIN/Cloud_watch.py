#!/usr/bin/env python3

import boto3
import json
from datetime import datetime, timedelta
import cgi
import cgitb

cgitb.enable()

print("Content-Type: application/json")
print()

# Get the form data
form = cgi.FieldStorage()

aws_access_key_id = form.getvalue('aws_access_key_id')
aws_secret_access_key = form.getvalue('aws_secret_access_key')
region_name = form.getvalue('region_name')
namespace = form.getvalue('namespace')
metric_name = form.getvalue('metric_name')
instance_id = form.getvalue('instance_id')

# Create a CloudWatch client
cloudwatch = boto3.client(
    'cloudwatch',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Define the time range for the metrics
end_time = datetime.utcnow()
start_time = end_time - timedelta(days=1)

# Call the get_metric_statistics method
response = cloudwatch.get_metric_statistics(
    Namespace=namespace,
    MetricName=metric_name,
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': instance_id
        },
    ],
    StartTime=start_time,
    EndTime=end_time,
    Period=300,  # Period in seconds (e.g., 300 seconds = 5 minutes)
    Statistics=['Average'],  # Type of statistics (e.g., Average, Sum, Maximum, Minimum, SampleCount)
    Unit='Percent'  # Unit of the metric
)

# Extract the retrieved data points and prepare JSON response
data_points = [{'Time': dp['Timestamp'].isoformat(), 'Average': dp['Average']} for dp in response['Datapoints']]
print(json.dumps(data_points))
