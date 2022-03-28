def lambda_handler(event, context):
    """
    This function handles adding a custom claim to the cognito ID token.
    """
    
    groups = event['request']['groupConfiguration']['groupsToOverride']
    
    groupsOverride = []
    for group in groups :
        groupsOverride.append(group.replace("_","/",1).lower())
    
    print('|'.join(groupsOverride))

    event["response"]["claimsOverrideDetails"] = { 
        "groupOverrideDetails": {
            "groupsToOverride": groupsOverride
        }
    }
 
    # return modified ID token to Amazon Cognito 
    return event
