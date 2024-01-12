import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    event_detail = event.get('detail')

    # Skip logging 'No detail key found' warning
    if not event_detail:
        return False

    try:
        logger.info(f"Event received: {event}")

        event_name = event_detail.get('eventName')
        if event_name != 'CreateLoginProfile':
            logger.warning(f"Unexpected event: {event_name}")
            return False

        response_elements = event_detail.get('responseElements')
        if not response_elements:
            logger.warning("No 'responseElements' found in the event")
            return False

        login_profile = response_elements.get('loginProfile')
        if not login_profile:
            logger.warning("No 'LoginProfile' found in the 'responseElements'")
            return False

        username = login_profile.get('userName')  # Ensure 'userName' matches the actual key name
        if not username:
            logger.warning("Username not found in 'LoginProfile'")
            return False

        # IAM client initialization
        iam = boto3.client('iam')

        # Specify the IAM group to which the user will be added
        group_name = 'EnableMFA'  # Replace with your existing IAM group name

        # Check if the user is already in the specified group
        response = iam.get_group(GroupName=group_name)
        users_in_group = response.get('Users', [])
        user_already_in_group = any(user['UserName'] == username for user in users_in_group)

        if user_already_in_group:
            logger.info(f"User {username} is already in group {group_name}")
        else:
            # Add the user to the specified group
            iam.add_user_to_group(GroupName=group_name, UserName=username)
            logger.info(f"User {username} added to group {group_name}")

        return True

    except Exception as e:
        logger.error(f"Something went wrong: {e}")
        return False
