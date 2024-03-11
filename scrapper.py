import requests
from bs4 import BeautifulSoup
import csv


def scrape_fbref(url):
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')

        player_name = soup.find(id='meta').find_next('span').text.strip()
        stats_table = soup.find('div', class_='stats_pullout')

        goals = soup.find('strong', string='Gls').find_next(
            'p').text.strip()
        assists = soup.find('strong', string='Ast').find_next(
            'p').text.strip()
        matches_played = soup.find(
            'strong', string='MP').find_next('p').text.strip()
        minutes_played = soup.find(
            'strong', string='Min').find_next('p').text.strip()

        expected_goals = soup.find(
            'strong', string='xG').find_next('p').text.strip()
        non_penalty_expected_goals = soup.find(
            'strong', string='npxG').find_next('p').text.strip()
        expeted_assists = soup.find(
            'strong', string='xAG').find_next('p').text.strip()

        shot_creating_actions = soup.find(
            'strong', string='SCA').find_next('p').text.strip()
        goal_creating_actions = soup.find(
            'strong', string='GCA').find_next('p').text.strip()

        with open(f'{player_name}_stats.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Player', 'Goals', 'Assists', 'Matches Played',
                             'Minutes Played', 'Expected Goals',
                             'Non Penalty Expected Goals', 'Expected Assists',
                             'Shot Creating Actions', 'Goal Creating Actions'])
            writer.writerow([player_name, goals, assists, matches_played,
                            minutes_played, expected_goals, non_penalty_expected_goals, expeted_assists, shot_creating_actions, goal_creating_actions])
        print(
            f'Data has been extracted and stored into "{player_name}_stats.csv"')
    else:
        print('Cannot extract Data')
