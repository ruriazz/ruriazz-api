import sib_api_v3_sdk
from core.app_config import app_config
from sib_api_v3_sdk.rest import ApiException

class SendInBlue:
    def __init__(self):
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = app_config.get('sib_key')
        _api_ = sib_api_v3_sdk.ApiClient(configuration)

        self._api_ = {
            'contact': sib_api_v3_sdk.ContactsApi(_api_),
            'email': sib_api_v3_sdk.TransactionalEmailsApi(_api_)
        }


    @staticmethod
    def create_contact(email: str, name: str = 'anonim') -> bool:
        sib = SendInBlue()
        api = sib._api_.get('contact')
        create_contact = sib_api_v3_sdk.CreateContact(
            email=email,
            update_enabled=True,
            attributes={
                'FNAME': name,
                'LNAME': 'ok'
            }
        )

        try:
            api.create_contact(create_contact)
            return True
        except ApiException as e:
            print("Exception when calling ContactsApi->create_contact: %s\n" % e)
            return False

    @staticmethod
    def send_email(subject: str, html_message: str, from_email: dict, reply_to: dict, receipents: dict) -> bool:
        sib = SendInBlue()
        api = sib._api_.get('email')

        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=[receipents],
            reply_to=from_email,
            html_content=html_message,
            sender=from_email,
            subject=subject
        )

        try:
            api.send_transac_email(send_smtp_email)
            return True
        except ApiException as e:
            print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
            return False