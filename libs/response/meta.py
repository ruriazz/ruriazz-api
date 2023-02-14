import re
from configs.variables import API_META


class APIMeta:
    success: bool
    code: int
    http_code: int
    message: str

    def __init__(self, contract: str = 'S1001') -> None:
        meta = API_META.get(contract)
        if meta:
            self.code = int(re.sub('[^0-9]', '', contract))
            self.http_code = meta[0]
            self.message = meta[1]
            self.success = meta[0] >= 100 and meta[0] < 299

    def _to_dict(self) -> dict:
        try: return {'success': self.success, 'code': self.code, 'httpCode': self.http_code, 'message': self.message}
        except: return {}