import requests
import json
import pandas 
import logging
import boto3
from io import StringIO

class ProcessApi:
    def __init__(self, item:str, req_list:list=None):
        self.item=item
        self.req_list=req_list
        with open('params.json', 'r') as f:
            config = json.load(f)
        self.url = config[item]["url"]
        self.api_key=config[item]["key"]
        self.bucket=config[item]["bucket"]
        try:
            self.filename=config[item]["filename"]
        except:
            self.filename=None

        self.payload = {}
        self.headers = {}

    def GetReq(self, filters:str=None):
        #TODO::: SET UP PAGES.
        try:
            #self.url1=self.url  + "?access_key=" +self.api_key
            if (filters):
                url1=self.url + "?/" + filters +"&" + "access_key=" +self.api_key
            else:
                url1=self.url +  "?"  + "access_key=" +self.api_key
            
            response_data = requests.get(url1)
            response_df=pandas.DataFrame(json.loads(response_data.text))

            #response review
            print(response_data.status_code)

        except:
            print(logging.exception)
        return response_df

    def NormData(self, data_df, norm_criteria):
        normdata=pandas.json_normalize(data_df[norm_criteria])
        print(normdata.columns)
        return normdata
    #TODO, MULTILEVEL NORM. NESTED STRUCTURES

    def S3Load(self,normdata, filename=None):
        if not (filename):
            filename=self.filename

        csv_buffer = StringIO()
        normdata.to_csv(csv_buffer)
        s3_resource = boto3.resource('s3')
        s3_resource.Object(self.bucket, filename).put(Body=csv_buffer.getvalue())        

    def iterProcessReq(self):
        for topic in self.topics:
            norm_criteria=topic["norm_criteria"]
            topic_data=self.GetReq(topic["tag"], topic["filters"])
            normdata=self.NormData(topic_data, norm_criteria)
            s3_load_status=self.S3Load(normdata, topic["file_name"])
            
    def DeleteS3File(self):
        s3 = boto3.resource('s3')
        if not (self.filename):
            for topic in self.topics:

                try:
                    s3.Object(self.bucket, topic["file_name"]).delete()
                except:
                    print("chose different topic")
        else:
                s3.Object(self.bucket, self.filename).delete()

def main():
    
    basic1=ProcessApi("exchange_basic") # simple exchange df
    #Process Instance1
    data=basic1.GetReq()
    wr=basic1.S3Load(data)
    del1=basic1.DeleteS3File()

if __name__=='__main__':
    main()