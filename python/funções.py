def enviar_email(nome,email):
    nome_dest = nome
    email_dest = email
    return f"Email enviado para {nome_dest}, Dono(a) do email {email_dest}"

pessoas = [
    {
        'nome': '{{nome.usuario}}',
        'email': '{{email.usuario}}'
    },
    {
        'nome': '{{nome.usuario}}',
        'email': '{{email.usuario}}'
    },
    {
        'nome': '{{nome.usuario}}',
        'email': '{{email.usuario}}'
    }
]

for pessoa in pessoas:
    email_enviado = enviar_email(pessoa['nome'], pessoa['email'])
    print(email_enviado)