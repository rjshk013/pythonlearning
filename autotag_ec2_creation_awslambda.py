import json
import boto3
import logging
import time
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ids = []
    try:
        logger.info(f"Event received: {event}")

        # Enhanced error handling for 'region'
        region = event.get('region')
        if not region:
            logger.error("Region not found in event")
            return False

        detail = event['detail']
        eventname = detail['eventName']
        arn = detail['userIdentity']['arn']
        principal = detail['userIdentity']['principalId']
        userType = detail['userIdentity']['type']

        if userType == 'IAMUser':
            user = detail['userIdentity']['userName']
        else:
            user = principal.split(':')[1]

        logger.info(f'principalId: {principal}')
        logger.info(f'region: {region}')
        logger.info(f'eventName: {eventname}')
        logger.info(f'detail: {detail}')

        if not detail.get('responseElements'):
            logger.warning('No responseElements found')
        if detail.get('errorCode'):
            logger.error(f'errorCode: {detail["errorCode"]}')
        if detail.get('errorMessage'):
            logger.error(f'errorMessage: {detail["errorMessage"]}')
            return False

        ec2 = boto3.resource('ec2')

        if eventname == 'RunInstances':
            items = detail['responseElements']['instancesSet']['items']
            for item in items:
                ids.append(item['instanceId'])
            creation_time = detail['eventTime']
            logger.info(f'number of instances: {len(ids)}')
        else:
            logger.warning('Not supported action')

        if ids:
            for resourceid in ids:
                print(f'Tagging resource {resourceid}')
                logger.info(f'ID Information:{ids}')
            ec2.create_tags(Resources=ids, Tags=[{'Key': 'Owner', 'Value': user},
                                                {'Key': 'PrincipalId', 'Value': principal},
                                                {'Key': 'arn', 'Value': arn},
                                                {'Key': 'Creation-Time', 'Value': creation_time}])

        logger.info(f'Remaining time (ms): {context.get_remaining_time_in_millis()}\\n')
        return True

    except Exception as e:
        logger.error(f'Something went wrong: {e}')
        return False
