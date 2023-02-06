API_META: dict = {
    # Success Contracts
    'S1000': (200, 'OK'),
    'S1001': (201, 'Data Created'),
    'S1002': (202, 'Authentication Success'),
    'S1003': (200, 'Authorization has been revoked'),


    # Error Contracts
    'E7000': (400, 'General Error'),
    'E7001': (400, 'Form validation error'),
    'E7002': (401, 'Authentication error'),
    'E7003': (401, 'No Authorization header'),
    'E7004': (401, 'Invalid Authorization header'),
    'E7005': (400, 'Parameter validation error'),
    'E7006': (401, 'Authorization expired'),
    'E7007': (400, 'Create Data Error'),
    'E7008': (400, 'Get Data Error'),
    'E7009': (401, 'Invalid Permission'),
    'E7010': (401, 'Account Inactive'),
    'E7011': (400, 'Data Not Found'),
    'E7012': (400, 'Submit Data Error'),
}