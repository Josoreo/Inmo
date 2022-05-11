import base64
import os
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
from sendgrid import SendGridAPIClient

message = Mail(
    from_email='gente.usuario@gmail.com',
    to_emails='jhpueyrredon@gmail.com',
    subject='Prueba inmo',
    html_content='<strong>Estimado cliente usted debe bastante dinero, vea el pdf adjunto</strong>')
"""file_path = 'example.pdf'
with open(file_path, 'rb') as f:
    data = f.read()
    f.close()
encoded = base64.b64encode(data).decode()
attachment = Attachment()
attachment.file_content = FileContent(encoded)
attachment.file_type = FileType('application/pdf')
attachment.file_name = FileName('Informacion.pdf')
attachment.disposition = Disposition('attachment')
attachment.content_id = ContentId('Example Content ID')
message.attachment = attachment
"""
try:
    sendgrid_client = SendGridAPIClient(os.environ.get('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'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)

