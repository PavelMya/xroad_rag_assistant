import os
from email.message import EmailMessage
import aiosmtplib
from dotenv import load_dotenv

load_dotenv()

async def send_db_via_email(to_email: str) -> bool:
    db_path = "interactions.db"
    if not os.path.exists(db_path):
        return False

    msg = EmailMessage()
    msg["From"] = os.getenv("EMAIL_FROM")
    msg["To"] = to_email
    msg["Subject"] = "X-Road Chat — DB Export"
    msg.set_content("Во вложении база данных вопросов и ответов.")

    with open(db_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="interactions.db"
        )

    try:
        await aiosmtplib.send(
            msg,
            hostname=os.getenv("EMAIL_HOST"),
            port=int(os.getenv("EMAIL_PORT")),
            username=os.getenv("EMAIL_HOST_USER"),
            password=os.getenv("EMAIL_HOST_PASSWORD"),
            start_tls=True
        )
        return True
    except Exception as e:
        print(f"Ошибка отправки: {e}")
        return False