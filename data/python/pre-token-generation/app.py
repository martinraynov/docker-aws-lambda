def lambda_handler(event, context):
    """
    This function handles adding a custom claim to the cognito ID token.
    """
    
    # grab requestor's email address
    email = event['request']['userAttributes']['email']
    
    # placeholder variable
    pet_preference = ''
    
    # set preference to 'dogs' if email contains @amazon.com
    # otherwise preference is 'cats'
    if "@amazon.com" in email:
        pet_preference = 'dogs'
    else:
        pet_preference = 'cats'
    
    # this allows us to override claims in the id token
    # "claimsToAddOrOverride" is the important part 
    event["response"]["claimsOverrideDetails"] = { 
        "claimsToAddOrOverride": { 
            "hove-test2": pet_preference 
            }
        } 
         
    # return modified ID token to Amazon Cognito 
    return event 