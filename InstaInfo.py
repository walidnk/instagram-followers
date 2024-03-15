import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import pandas as pd
import time
from datetime import datetime


class Insta_Info_Scraper:

    # Remove the user account for use
    # def get_name(self, user):
    #     input_string = user

    #     start_pos = input_string.find('(')
    #     name_chars = []
    #     for i in range(0, start_pos):
    #         name_chars.append(input_string[i])
    #     name = ''.join(name_chars)
    #     return name

    def getinfo(self, url):
        html = urllib.request.urlopen(url, context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all('meta', attrs={'property': 'og:description'})
        text = data[0].get('content').split()
        user = '%s %s' % (text[-3], text[-2])
        followers = text[0]
        following = text[2]
        posts = text[4]
        email = ""
        print('User:', user)
        print('Followers:', followers)
        print('Following:', following)
        print('Posts:', posts)
        print('Email:', email)
        print('---------------------------')
        return user, followers

    def main(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

        # with open('links.txt') as f:
        #     self.content = f.readlines()
        # self.content = [x.strip() for x in self.content]

        self.content = pd.read_csv('links.csv')

        # Create a dataframe
        columns = ['Nombre', 'Categoria', 'Campaña',
                   'Link de Instagram', 'E-mail', 'Status', 'Numero de seguidores']
        profile_df = pd.DataFrame(columns=columns)

        # Get the current date
        current_date = datetime.now()

        # Format the date as "Month Day"
        formatted_date = current_date.strftime("%B %d")
        date = f'Sent 1st - {formatted_date}'
        # for url in self.content:
        for idx, row in self.content.iterrows():
            url = row['user_links']
            if url != '':
                time.sleep(5)
                name, followers = self.getinfo(url)
                profile_df.loc[len(profile_df.index)] = [
                    name, row['category'], ' ', url, ' ', date, followers]
        profile_df.to_excel(
            f'Lista {datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.xlsx')


if __name__ == '__main__':
    obj = Insta_Info_Scraper()
    obj.main()
