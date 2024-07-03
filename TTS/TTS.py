import datetime
import os
import json
from gtts import gTTS
import pygame
from anthropic import Anthropic
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# 설정 파일 경로
CONFIG_FILE = "diary_config.json"

# 전역 변수로 저장 경로 설정
SAVE_PATH = ""

# Anthropic 클라이언트 설정 미결재 사용 불가
anthropic = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def load_config():
    global SAVE_PATH
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            SAVE_PATH = config.get("save_path", "")
    if not SAVE_PATH or not os.path.exists(SAVE_PATH):
        SAVE_PATH = os.getcwd()  # 기본값으로 현재 작업 디렉토리 사용

def save_config():
    config = {"save_path": SAVE_PATH}
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def set_save_path():
    global SAVE_PATH
    new_path = input("새로운 저장 경로를 입력하세요: ")
    if os.path.exists(new_path):
        SAVE_PATH = new_path
        save_config()
        print(f"저장 경로가 {SAVE_PATH}로 변경되었습니다.")
    else:
        print("유효하지 않은 경로입니다. 기존 경로를 유지합니다.")

def get_file_path(filename):
    return os.path.join(SAVE_PATH, filename)

def get_unique_filename(base_filename):
    counter = 1
    filename, ext = os.path.splitext(base_filename)
    while os.path.exists(get_file_path(base_filename)):
        base_filename = f"{filename}_{counter}{ext}"
        counter += 1
    return base_filename

def write_diary():
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f"\n{date} 일기 작성")
    entry = input("오늘의 일기를 작성하세요: ")
    
    base_filename = f"diary_{date}.txt"
    filename = get_unique_filename(base_filename)
    full_path = get_file_path(filename)
    with open(full_path, "w", encoding="utf-8") as file:
        file.write(entry)
    
    print(f"일기가 {full_path}에 저장되었습니다.")
    return full_path, entry

def read_diary(filename):
    full_path = get_file_path(filename)
    with open(full_path, "r", encoding="utf-8") as file:
        return file.read()

def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='ko')
    audio_filename = filename.replace(".txt", ".mp3")
    audio_filename = get_unique_filename(audio_filename)
    full_path = get_file_path(audio_filename)
    tts.save(full_path)
    print(f"음성 파일이 {full_path}에 저장되었습니다.")
    return full_path

def play_audio(audio_filename):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def list_diary_files():
    files = [f for f in os.listdir(SAVE_PATH) if f.startswith("diary_") and f.endswith(".txt")]
    return sorted(files)

def select_diary_file(files):
    while True:
        print("\n저장된 일기 목록:")
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")
        
        choice = input("읽고 싶은 일기의 번호 또는 날짜(YYYYMMDD)를 입력하세요: ")
        
        if choice.isdigit() and 1 <= int(choice) <= len(files):
            return files[int(choice) - 1]
        else:
            try:
                date = datetime.datetime.strptime(choice, "%Y%m%d").strftime("%Y-%m-%d")
                matching_files = [f for f in files if f.startswith(f"diary_{date}")]
                if matching_files:
                    if len(matching_files) == 1:
                        return matching_files[0]
                    else:
                        print(f"\n{date}에 해당하는 일기:")
                        for i, file in enumerate(matching_files, 1):
                            print(f"{i}. {file}")
                        sub_choice = input("선택할 일기의 번호를 입력하세요: ")
                        if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(matching_files):
                            return matching_files[int(sub_choice) - 1]
                        else:
                            print("유효하지 않은 번호입니다. 다시 시도해주세요.")
                else:
                    print(f"{date}에 해당하는 일기가 없습니다. 다시 시도해주세요.")
            except ValueError:
                print("유효하지 않은 입력입니다. 번호 또는 YYYYMMDD 형식의 날짜를 입력해주세요.")
        
        print("다시 선택해주세요.")

def claude_search(query):
    if not os.getenv("ANTHROPIC_API_KEY"):
        return "Error: ANTHROPIC_API_KEY가 설정되지 않았습니다. .env 파일을 확인해주세요."
    
    try:
        response = anthropic.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            messages=[
                {"role": "user", "content": query}
            ]
        )
        return response.content[0].text
    except Exception as e:
        return f"Claude 3.5 Sonnet 검색 중 오류가 발생했습니다: {str(e)}"

def main():
    load_config()
    print(f"현재 저장 경로: {SAVE_PATH}")
    
    while True:
        print("\n1. 일기 쓰기 (즉시 음성 출력)")
        print("2. 일기 읽기")
        print("3. 저장된 일기 음성으로 듣기")
        print("4. 저장 경로 변경")
        print("5. Claude 3.5 Sonnet으로 검색하기")
        print("6. 종료")
        
        choice = input("원하는 작업을 선택하세요 (1-6): ")
        
        if choice == "1":
            filename, entry = write_diary()
            print("일기를 음성으로 변환 중...")
            audio_filename = text_to_speech(entry, filename)
            print("변환된 일기를 재생합니다.")
            play_audio(audio_filename)
        elif choice == "2":
            files = list_diary_files()
            if files:
                selected_file = select_diary_file(files)
                print(read_diary(selected_file))
            else:
                print("저장된 일기가 없습니다.")
        elif choice == "3":
            files = list_diary_files()
            if files:
                selected_file = select_diary_file(files)
                text = read_diary(selected_file)
                audio_filename = text_to_speech(text, selected_file)
                print("저장된 일기를 재생합니다.")
                play_audio(audio_filename)
            else:
                print("저장된 일기가 없습니다.")
        elif choice == "4":
            set_save_path()
        elif choice == "5":
            query = input("Claude 3.5 Sonnet에게 물어볼 내용을 입력하세요: ")
            result = claude_search(query)
            print("\nClaude 3.5 Sonnet 응답:")
            print(result)
        elif choice == "6":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()