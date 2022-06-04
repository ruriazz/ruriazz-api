import html, requests
from pyclbr import Function
from rest_framework.request import Request
from core.app_config import app_config

from validators.strings.valid_email import valid_email

def is_post_mail_hook(function: Function) -> Function:
    def wrapper(request: Request, *args, **kwargs):
        request.error_data = None
        data = request.data
        errors = {}
        temp_data = {
            'token': data.get('token').strip() if isinstance(data.get('token', ''), str) and len(data.get('token', '')) > 0 else None,
            'sender_name': data.get('sender_name').strip() if isinstance(data.get('sender_name', ''), str) and len(data.get('sender_name', '')) > 0 and len(data.get('sender_name')) < 50 else None,
            'sender_email': data.get('sender_email').strip() if isinstance(data.get('sender_email', ''), str) and valid_email(data.get('sender_email', '')) else None,
            'message': html.escape(str(data.get('message')).strip()) if len(str(data.get('message', ''))) > 0 and len(str(data.get('message', ''))) < 300 else None
        }

        if not temp_data.get('token'):
            errors['token'] = 'is_required'

        if not temp_data.get('sender_name'):
            errors['sender_name'] = 'invalid'

        if not temp_data.get('sender_email'):
            errors['sender_email'] = 'invalid'

        if not temp_data.get('message'):
            errors['message'] = 'invalid'

        if len(errors) > 0:
            request.error_data = errors
        else:
            if len(temp_data.get('token')) < 255:
                request.error_data = {
                    'token': 'invalid'
                }
            else:    
                response = requests.post(
                    url='https://hcaptcha.com/siteverify',
                    data={
                        'response': temp_data.get('token'),
                        'sitekey': app_config.get('hcaptcha_sitekey'),
                        'secret': app_config.get('hcaptcha_secret')
                    }
                )
                
                if response.status_code == 200:
                    response_data = response.json()

                    if not response_data.get('success', False):
                        request.error_data = {
                            'token': 'invalid'
                        }

                    else:
                        temp_data['token'] = response_data
                    

        request.valid_data = temp_data
        func = function(request, *args, **kwargs)
        return func
        

    return wrapper