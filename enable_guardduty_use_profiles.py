"""

Enables GuardDuty delegated administrator account
across all aws regions
RUN THIS AS YOUR ORG MASTER

Python Version: 3.7.0
Boto3 Version: 1.7.50

"""

import boto3, sys
from botocore.exceptions import ClientError

guarddutyadminaccount = '123456789012' #change this to your real account

def get_regions(ec2):
  """
  Return all AWS regions
  """

  regions = []

  try:
    aws_regions = ec2.describe_regions()['Regions']
  except ClientError as e:
    print(e.response['Error']['Message'])

  else:
    for region in aws_regions:
      regions.append(region['RegionName'])

  return regions


def main(profile):
  """
  Do the work..

  Order of operation:

  1.) Get the available aws regions
  2.) Delegate GuardDuty Administrator to the specified account
  """

  # AWS Credentials
  # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html

  session = boto3.Session(profile_name=profile)
  ec2 = session.client('ec2', region_name='us-east-1')

  regions = get_regions(ec2)

  for region in regions:

    gd = session.client('guardduty', region_name=region)

    try:
      result = gd.enable_organization_admin_account(
        AdminAccountId=guarddutyadminaccount
      )
    except ClientError as e:
      print(e.response['Error']['Message'])
    
    else:
      print('Account {} has been enabled in {} region '.format(guarddutyadminaccount, region))

  return

if __name__ == "__main__":
  if(len(sys.argv)) >= 2:
    try: 
      main(profile = sys.argv[1])
    except Exception as e: print(e)
  else: 
    print("you must provide an account profile name")

# if __name__ == "__main__":
#   try: 
#     main()
#   except Exception as e: print(e)
