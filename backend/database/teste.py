import requests

headers = {
    "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4IiwiZXhwIjoxNzU2Mjk4NzgzfQ.oKcK-PMAAFeU5moQ4IazrdMp9oI12iaNytnQ_DTShJo"
}

requesicao=requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers )

print(requesicao)
print(requesicao.json())