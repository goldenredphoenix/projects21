from email.mime.multipart import MIMEMultipart

from src.config_6 import SMTPSettings
from src.email_6 import EmailMessage


def main() -> MIMEMultipart:
    """Спрашивает почту пациента, создаёт письмо, возвращает MIME."""

    # 1. Читаем SMTP-настройки
    smtp_config: SMTPSettings = SMTPSettings()

    # 2. Спрашиваем почту пациента
    patient_email: str = input("Enter patient email: ")

    # 3. Создаём письмо
    email_message: EmailMessage = EmailMessage(
        from_email=smtp_config.email,
        to_email=patient_email,
        subject="Receipt",
        body="Test",
    )

    # 4. Упаковываем в MIME
    mime_message: MIMEMultipart = email_message.create_mime_message()

    # 5. Возвращаем
    return mime_message


if __name__ == "__main__":
    main()