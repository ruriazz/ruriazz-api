## ruriazz API Short Documentations

### Webhook
- **Forward contact to email** <br />
Method: **POST** <br />
Path: `/hook/mail` <br />
Data: `Content-Type`: `application/xml`
```
<?xml version="1.0" encoding="utf-8"?>
<root>
	<sender_name>SENDER_EMAIL</sender_name>
	<sender_email>SENDER_EMAIL</sender_email>
	<message>MESSAGE</message>
	<token>RESPONSE_TOKEN</token>
</root>
```
