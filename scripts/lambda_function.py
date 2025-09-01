import json
import random
import os
import boto3
from datetime import datetime, timedelta
from scripts.generate_data import *

def lambda_handler(event, context):
    try:
        # Yesterday's date
        yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        num_rows = random.randint(1000, 2000)
        
        # Generate fake data
        fake_data = generate_fake_data()
        
        # Generate rows
        rows = generate_data_rows(num_rows, yesterday, fake_data)
        
        # Write to /tmp
        file_name = f"orders_{yesterday}.csv"
        tmp_path = f"/tmp/{file_name}"
        write_csv(rows, tmp_path)
        
        print(f"Generated {num_rows} rows for {yesterday}")
        
        # Upload to S3
        bucket_name = os.environ["BUCKET_NAME"]
        s3 = boto3.client("s3")
        s3.upload_file(tmp_path, bucket_name, file_name)
        
        print(f"Uploaded to s3://{bucket_name}/{file_name}")
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "status": "success", 
                "rows": num_rows, 
                "file": file_name
            })
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "status": "error",
                "message": str(e)
            })
        }
