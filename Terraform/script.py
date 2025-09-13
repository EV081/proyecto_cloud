home = Path.home()
aws_dir = home / ".aws"
aws_dir.mkdir(exist_ok=True)

print("Introduce las credenciales temporales del Learner Lab:")
ak = input("AWS_ACCESS_KEY_ID: ").strip()
sk = input("AWS_SECRET_ACCESS_KEY: ").strip()
st = input("AWS_SESSION_TOKEN: ").strip()
region = input("AWS_DEFAULT_REGION (ej. us-east-1): ").strip() or "us-east-1"

credentials = f"""[default]
aws_access_key_id = {ak}
aws_secret_access_key = {sk}
aws_session_token = {st}
"""
config = f"""[default]
region = {region}
output = json
"""

(aws_dir / "credentials").write_text(credentials)
(aws_dir / "config").
write_text(config)
print(f"Escrito {aws_dir/'credentials'} y {aws_dir/'config'}")

