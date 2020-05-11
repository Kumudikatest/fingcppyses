import boto3
ses = boto3.client("ses")

def handler(request):
    try:
        data = ses.send_email(
            Source="kumudika@adroitlogic.com",
            Destination={
                'ToAddresses': ["kumudika@adroitlogic.com"]
            },
            Message={
                'Subject': {
                    'Data': "test"
                },
                'Body': {
                    'Text': {
                        'Data': ""
                    }
                }
            }
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return "Successfully executed"
