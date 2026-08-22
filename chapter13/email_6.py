from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailMessage:
    """Класс письма. Хранит данные и создаёт MIME-сообщение."""

    from_email: str
    to_email: str
    subject: str
    body: str

    def __init__(
        self,
        from_email: str,
        to_email: str,
        subject: str,
        body: str,
    ) -> None:
        self.from_email: str = from_email
        self.to_email: str = to_email
        self.subject: str = subject
        self.body: str = body

    def create_mime_message(self) -> MIMEMultipart:
        """Создаёт и возвращает MIME-сообщение."""
        msg: MIMEMultipart = MIMEMultipart()

        msg["From"] = self.from_email
        msg["To"] = self.to_email
        msg["Subject"] = self.subject

        msg.attach(MIMEText(self.body, "plain"))

        return msg