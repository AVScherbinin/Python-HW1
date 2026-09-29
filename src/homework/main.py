import hashlib
import smtplib
from email.message import EmailMessage
from getpass import getpass


FIO = "Щербинин Антон Владимирович"
EMAIL_FROM = "avshcherbinin@edu.hse.ru"
SMTP_HOST = "smtp.yandex.ru"
SMTP_PORT = 465


def calculate_hashes(text: str) -> tuple[str, str]:
    text_bytes = text.encode("utf-8")

    md5_hash = hashlib.md5(text_bytes).hexdigest()
    sha256_hash = hashlib.sha256(text_bytes).hexdigest()

    return md5_hash, sha256_hash


def send_email(
    recipient: str,
    md5_hash: str,
    sha256_hash: str,
) -> None:
    password = getpass("Введите пароль приложения: ")

    message = EmailMessage()
    message["Subject"] = "Результат задания homework-01"
    message["From"] = EMAIL_FROM
    message["To"] = recipient

    message.set_content(
        f"""ФИО: {FIO}

MD5:
{md5_hash}

SHA-256:
{sha256_hash}
"""
    )

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(EMAIL_FROM, password)
        server.send_message(message)


def main() -> None:
    x = 1
    y = 3.14
    z = True
    name = "Python"
    numbers = [1, 2, 3]
    coordinates = (10, 20)
    unique_numbers = {1, 2, 3}
    person = {"name": "Anton", "age": 28}

    report = (
        f"x = {x}, type = {type(x)}\n"
        f"y = {y}, type = {type(y)}\n"
        f"z = {z}, type = {type(z)}\n"
        f"name = {name}, type = {type(name)}\n"
        f"numbers = {numbers}, type = {type(numbers)}\n"
        f"coordinates = {coordinates}, type = {type(coordinates)}\n"
        f"unique_numbers = {unique_numbers}, type = {type(unique_numbers)}\n"
        f"person = {person}, type = {type(person)}\n"
        f"ФИО: {FIO}"
    )

    md5_hash, sha256_hash = calculate_hashes(report)

    print(report)
    print()
    print("MD5:", md5_hash)
    print("SHA-256:", sha256_hash)

    recipient = input("\nВведите адрес получателя: ")

    send_email(recipient, md5_hash, sha256_hash)

    print("Письмо успешно отправлено!")


if __name__ == "__main__":
    main()
