import boto3

s3 = boto3.client('s3')
#s3.list_objects()

s3.upload_file('C:/Users/preco/OneDrive/Desktop/AiCore/Web_Scraping/raw_data2/images/image0.png', 'scraperbucket1000', 'image0.png')