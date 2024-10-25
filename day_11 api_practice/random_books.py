import requests


def rendom_book_genrate():
    url ='https://api.freeapi.app/api/v1/public/books/book/random'
    response = requests.get(url)
    data = response.json()
    if data['success'] and 'data' in data:
        book_data  = data['data']
        authors = book_data['volumeInfo']['authors'][0]
        title = book_data['volumeInfo']['title']
        return authors,title
    else:
        raise Exception("Not fetch api")
    

def main():
    try:
        authors,title = rendom_book_genrate()
        print(f"authors : {authors}\ntiltle : {title}")
    except Exception as e:
        print(str(e))


if  __name__ =="__main__":
    main()