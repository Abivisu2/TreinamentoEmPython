import requests

def main():
    url = 'https://www.python.org'
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        print(response.text)
    else:
        print("página não encontrada. Status code:", response.status_code)

if __name__ == '__main__':
    main() 
