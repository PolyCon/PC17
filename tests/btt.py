import boto3
def main():
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)
    data = open("../static/slide.png", "rb")
    s3.Bucket("polycon").put_object(Key="slide.png", Body=data)