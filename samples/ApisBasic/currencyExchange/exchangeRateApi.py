import requests
import json
import pandas 
import logging
import boto3

class ProcessApi:
    def __init__(self, item:str, req_list:list=None):
        self.item=item
        self.req_list=req_list
        with open('params.json', 'r') as f:
            config = json.load(f)
        self.url = config[item]["url"]
        self.api_key=config[item]["key"]
        self.topics=config[item]["request_"]
        self.bucket=config["bucket"]

        self.payload = {}
        self.headers = {}

    def GetReq(self, tag, filters):
        #TODO::: SET UP PAGES.
        try:

            url1=self.url + tag + "?/" + filters +"&" + "api_key=" +self.api_key
            response_data = requests.request("GET", url1, headers=self.headers, data=self.payload)
            response_df=pandas.DataFrame(json.loads(response_data.text))
        except:
            print(logging.exception)
        return response_df

    def NormData(self, data_df, norm_criteria):
        normdata=pandas.json_normalize(data_df[norm_criteria])
        return normdata
    #TODO, MULTILEVEL NORM. NESTED STRUCTURES

    def S3Load(self,normdata,filename):
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
        for topic in self.topics:
            s3 = boto3.resource('s3')
            s3.Object(self.bucket, topic["file_name"]).delete()

 