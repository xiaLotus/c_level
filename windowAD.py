from flask import Flask, request
import kerberos

app = Flask(__name__)

@app.route('/auth')
def authenticate():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return "Unauthorized", 401, {'WWW-Authenticate': 'Negotiate'}

    try:
        result, context = kerberos.authGSSServerInit('HTTP@yourserver.domain.com')
        kerberos.authGSSServerStep(context, auth_header.split()[1])
        user = kerberos.authGSSServerUserName(context)
        kerberos.authGSSServerClean(context)
        return f"Authenticated as {user}"
    except kerberos.KrbError:
        return "Unauthorized", 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# from flask import Flask, request
# from requests_ntlm import HttpNtlmAuth

# app = Flask(__name__)

# @app.route('/auth')
# def authenticate():
#     username = request.environ.get("REMOTE_USER")  # IIS 或其他反向代理需設定 Windows Auth
#     if not username:
#         return "Unauthorized", 401
#     return f"Authenticated as {username}"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
