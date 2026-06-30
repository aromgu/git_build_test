import requests



def say_hello(text: str):
    data = {
        "content": text
    }    
    requests.post(webhook_url, json=data)

if __name__ == "__main__":
    say_hello("ㅇㅅㅇ")
