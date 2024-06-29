import random
from datetime import date, timedelta
import csv
import os
import requests
from bs4 import BeautifulSoup

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

# 메인 코드
today = date.today()
num_sets = int(input("몇 세트의 로또 번호를 추천받으시겠습니까? "))

print(f"\n{today} 추천 로또 번호:")

data_to_save = []

for i in range(num_sets):
    numbers, bonus = generate_lotto_numbers()
    print(f"세트 {i+1}: {numbers}, 보너스 번호: {bonus}")
    
    data_to_save.append([today, i+1, numbers, bonus])

filename = 'lotto_recommendations.csv'
save_to_csv(data_to_save, filename)

print(f"\n추천 번호가 {filename} 파일에 저장되었습니다.")

# 당첨 번호 확인
current_draw_no, next_draw_date = calculate_draw_number(today)
if today < next_draw_date:
    print(f"\n현재 회차는 아직 추첨되지 않았습니다. 다음 추첨 날짜는 {next_draw_date} 입니다.")
else:
    print(f"\n현재 회차는 {current_draw_no} 입니다.")
    winning_numbers, winning_bonus = get_lotto_numbers(current_draw_no)
    print(f"\n{current_draw_no}회차 당첨 번호: {winning_numbers}, 보너스 번호: {winning_bonus}")

    for i, (_, _, numbers, bonus) in enumerate(data_to_save):
        result = check_winning(numbers, bonus, winning_numbers, winning_bonus)
        print(f"세트 {i+1} 결과: {result}")
