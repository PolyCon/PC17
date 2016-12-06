import boto3
import boto.s3
from PIL import Image

class bt:
    def __init__(self):
        self.s3 = boto3.resource('s3')
        self.conn = boto.s3.connect_to_region('us-east-1')
        self.bucket = self.conn.get_bucket("polycon")
    def getBuckets(self):
        return self.s3.buckets.all()
    def upload(self, floc, fname=None):
        if fname == None:
            fname = floc.split("/")[-1]
        data = open(floc, "rb")
        self.s3.Bucket("polycon").put_object(Key=fname, Body=data)
        key = self.bucket.lookup(fname)
        key.set_acl("public-read")
        url = key.generate_url(expires_in=0, query_auth=False)
        data.close()
        return url
    def resize(self, imf, height, oname=None):
        if oname == None:
            oname = imf.split("/")[-1]
        image = Image.open(imf, "r")
        oh, ow = image.size
        width = int(height * (ow/oh))
        image = image.resize((height, width), Image.ANTIALIAS)
        image.save("tmp/" + oname.split(".")[0] + "_" + str(height) + "." + oname.split(".")[-1])
        imloc = "tmp/" + oname.split(".")[0] + "_" + str(height) + "." + oname.split(".")[-1]
        return self.upload(imloc)