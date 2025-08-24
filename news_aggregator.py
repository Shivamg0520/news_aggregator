import requests
from bs4 import BeautifulSoup
import json

def save_data():
    with open('news_data.json', 'w') as file:
        json.dump(list_of_news_1, file, indent=4, )
        print("Data saved successfully")

def load_data():
    try:
        with open('news_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

list_of_news_1 = load_data()

def jagran():    
    url = "https://www.jagran.com/"
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'html.parser')
    data = soup.find_all('article',class_= 'CardStory__text')
    # print(news)
    
    for item in data:
        http = "https://www.jagran.com"
        urls = item.find('a')['href']
        # print(urls)
        link2 = http + urls
        # print(link2)
        responce2 = requests.get(link2)
        soup2 = BeautifulSoup(responce2.text,'html.parser')
        data2 = soup2.find_all('div',class_='ArticleDetail')
        # print(data2)
        for item2 in data2:
            title = item2.find('h1').text.strip()
            # print(f"Headline: {title}\n")
            short_summary = item2.find('p', class_='ArticleDetail_ArticleDetail__shortdescription__uLfAR').text.strip()
            # print(f"short summary: {short_summary}\n")
            full_summart = item2.find('div', class_='ArticleBody').text
            # print(f"full summary: {full_summart}\n\n")
            list_of_news_1.append({'title': title, 'link': link2,'short_summary': short_summary, 'full_summmary': full_summart})
            
def aajtak():    
    url = "https://aajtak.in/"
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'html.parser')
    data = soup.find_all('div',class_= 'player-sec')
    # print(data)
    for item in data:
        urls = item.find('a')['href']
        # print(urls)
        responce2 = requests.get(urls)
        soup2 = BeautifulSoup(responce2.text,'html.parser')
        data2 = soup2.find_all('div',class_='story-container')
        # print(data2)
        for item2 in data2:
            title = item2.find('h1').text.strip()
            # print(f"Headline: {title}\n")
            short_summary = item2.find('h2').text.strip()
            soup3 = soup2.find_all('div',class_='text-formatted')
            for item3 in soup3:
                a = item3.find_all('p')
                full_summart =''
                for para in a:
                    full_summart += para.text.strip()
            list_of_news_1.append({'title': title, 'link': urls,'short_summary': short_summary, 'full_summmary': full_summart})

def showing_data():
    for news in list_of_news_1:
        print(f"Title:{news['title']}\n\nLink: {news['link']}\n\nShort summary: {news['short_summary']}\n\nFull summary: {news['full_summmary']}\n\n\n")

def main():
    jagran()
    aajtak()
    
print("1: Jagran se news scrape karen\n2: Aajtak se news scrape kare\n3. Both\n4: Saved news dekhen\n5: Exit")
while True:
    user_input = input("\nEnter your choice: ")
    if user_input == '1':
        print("Scraping start from jagran")
        jagran()
        save_data()
        print(f"Total {len(list_of_news_1)} news scraped")
        print("complete")
    elif user_input == '2':
        print("Scraping start from aajtak")
        aajtak()
        save_data()
        print(f"Total {len(list_of_news_1)} news scraped")
        print("complete")
    elif user_input == '3':
        print("Scraping start from both jagran and aajtak")
        main()
        save_data()
        print(f"Total {len(list_of_news_1)} news scraped")
        print("complete")
    elif user_input == '4':
        if not list_of_news_1:
            print("No data available. Please scrape news first")
        else:
            showing_data()
    elif user_input == '5':
        while 1:
            confirmation_input = input('are you sure you want to exit? (y/n): ')
            if confirmation_input.lower() == 'y':
                exit()
            elif confirmation_input.lower() == 'n':
                break
            else:
                print("Invalid input")
    else:
        print("Invalid input")
