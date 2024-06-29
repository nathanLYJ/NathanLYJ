from flask import Flask, render_template, request
import random
from datetime import date, timedelta
import csv
import os
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def generate_lotto_numbers():
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    bonus = random.choice([num for num in range(1, 46) if num not in numbers])
    return numbers, bonus

def save_to_csv(data, filename):
    file_exists = os.path.isfile(filename)
    
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(['Date', 'Set', 'Numbers', 'Bonus'])
        writer.writerows(data)

def get_lotto_numbers(draw_no):
    url = f"https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo={draw_no}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    numbers = soup.select('span.ball_645')
    winning_numbers = [int(num.text) for num in numbers[:6]]
    bonus_number = int(numbers[6].text)
    
    return winning_numbers, bonus_number

def check_winning(my_numbers, my_bonus, winning_numbers, winning_bonus):
    matched = set(my_numbers) & set(winning_numbers)
    if len(matched) == 6:
        return "1등"
    elif len(matched) == 5 and my_bonus == winning_bonus:
        return "2등"
    elif len(matched) == 5:
        return "3등"
    elif len(matched) == 4:
        return "4등"
    elif len(matched) == 3:
        return "5등"
    else:
        return "낙첨"

def calculate_draw_number(current_date):
    start_date = date(2002, 12, 7)  # Assume the first draw was on December 7, 2002 (Saturday)
    days_since_start = (current_date - start_date).days
    draw_number = (days_since_start // 7) + 1
    next_draw_date = start_date + timedelta(weeks=draw_number)
    
    if current_date < next_draw_date:
        return draw_number - 1, next_draw_date
    return draw_number, next_draw_date

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    num_sets = int(request.form['num_sets'])
    today = date.today()
    data_to_save = []

    recommendations = []
    for i in range(num_sets):
        numbers, bonus = generate_lotto_numbers()
        recommendations.append({'set': i+1, 'numbers': numbers, 'bonus': bonus})
        data_to_save.append([today, i+1, numbers, bonus])

    save_to_csv(data_to_save, 'lotto_recommendations.csv')
    return render_template('recommend.html', recommendations=recommendations, date=today)

@app.route('/check', methods=['POST'])
def check():
    today = date.today()
    current_draw_no, next_draw_date = calculate_draw_number(today)
    
    if today < next_draw_date:
        return render_template('check.html', message=f"현재 회차는 아직 추첨되지 않았습니다. 다음 추첨 날짜는 {next_draw_date} 입니다.")
    else:
        winning_numbers, winning_bonus = get_lotto_numbers(current_draw_no)
        return render_template('check.html', draw_no=current_draw_no, winning_numbers=winning_numbers, winning_bonus=winning_bonus)

if __name__ == '__main__':
    app.run(debug=True)
