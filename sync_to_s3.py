import boto3

filename = 'index.html'
foldername = 'shiraz/trading_system_v3/dashboard/'
s3 = boto3.resource('s3')
s3.Bucket('shirazhazrat.com').upload_file(
	filename, filename, ExtraArgs={'ACL': 'public-read', 'ContentType': 'text/html'})
print('Uploaded index.html to s3://shirazhazrat.com/index.html')