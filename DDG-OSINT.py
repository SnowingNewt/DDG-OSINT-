import requests
from bs4 import BeautifulSoup
import random
import random
import colorama
import os

colorama.init()


def main():
    # Rainbow color codes
    colors = [
        "\033[1;31;40m",
        "\033[1;33;40m",
        "\033[1;32;40m",
        "\033[1;34;40m",
        "\033[1;35;40m",
        "\033[1;36;40m",
    ]

    # ASCII art
    art = [
        "██████╗ ██████╗  ██████╗      ██████╗ ███████╗██╗███╗   ██╗████████╗",
        "██╔══██╗██╔══██╗██╔════╝     ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝",
        "██║  ██║██║  ██║██║  ███╗    ██║   ██║███████╗██║██╔██╗ ██║   ██║   ",
        "██║  ██║██║  ██║██║   ██║    ██║   ██║╚════██║██║██║╚██╗██║   ██║   ",
        "██████╔╝██████╔╝╚██████╔╝    ╚██████╔╝███████║██║██║ ╚████║   ██║   ",
        "╚═════╝ ╚═════╝  ╚═════╝      ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   ",
  ]

    # Print ASCII art in rainbow colors
    for line in art:
        color = random.choice(colors)
        print(color + line)

    # Print creator in highlighted color
    print("\033[1;31;40mCreated by David Mascaro\033[0m")

if __name__ == "__main__":
    main()
def search_duckduckgo(query, num_results):
    """
    Searches DuckDuckGo for the given query and returns a DataFrame with the results
    """
    url = f'https://duckduckgo.com/html/?q={query}&kl=br-pt&k1=-1&kj=br-pt&kp=-1&kr=br-pt&kx=b&kf=-1&kaf=1&kt=a&kak=-1&kax=-1&kaq=-1&kap=-1&kao=-1&kau=-1&k1=-1&kaj=m&kam=osm&kai=1&kae=d&kau=-1&k1=-1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', class_='result__url')

    results = []
    for link in links[:num_results]:
        title = link.find_previous('h2', class_='result__title').get_text().strip()
        url = link['href']
        results.append((title, url))

    return results


def main():
    query = input('Digite a sua busca: ')
    num_results = int(input('Quantos resultados você deseja? '))

    results = search_duckduckgo(query, num_results)

    # Escreve os resultados em um arquivo
    with open('results.txt', 'w', encoding='utf-8') as f:
        f.write('+----------------------------------------------------------+\n')
        f.write('|{:>30} | {:<50}|\n'.format('Title', 'URL'))
        f.write('+------------------------------+-----------------------------------+\n')
        for i, result in enumerate(results, start=1):
            f.write('|{:>2}. {:<27} | {:<50}|\n'.format(i, result[0][:27], result[1]))
        f.write('+----------------------------------------------------------+\n')


if __name__ == '__main__':
    main()
