import datetime
import os
from gtts import gTTS
import pygame

def write_diary():
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f"\n{date} 일기 작성")
    entry = input("오늘의 일기를 작성하세요: ")
    
    filename = f"diary_{date}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(entry)
    
    print(f"일기가 {filename}에 저장되었습니다.")
    return filename, entry

def read_diary(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='ko')
    audio_filename = filename.replace(".txt", ".mp3")
    tts.save(audio_filename)
    print(f"음성 파일이 {audio_filename}에 저장되었습니다.")
    return audio_filename

def play_audio(audio_filename):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    while True:
        print("\n1. 일기 쓰기 (즉시 음성 출력)")
        print("2. 일기 읽기")
        print("3. 저장된 일기 음성으로 듣기")
        print("4. 종료")
        
        choice = input("원하는 작업을 선택하세요 (1-4): ")
        
        if choice == "1":
            filename, entry = write_diary()
            print("일기를 음성으로 변환 중...")
            audio_filename = text_to_speech(entry, filename)
            print("변환된 일기를 재생합니다.")
            play_audio(audio_filename)
        elif choice == "2":
            date = input("읽고 싶은 일기의 날짜를 입력하세요 (YYYY-MM-DD): ")
            filename = f"diary_{date}.txt"
            if os.path.exists(filename):
                print(read_diary(filename))
            else:
                print("해당 날짜의 일기가 존재하지 않습니다.")
        elif choice == "3":
            date = input("듣고 싶은 일기의 날짜를 입력하세요 (YYYY-MM-DD): ")
            filename = f"diary_{date}.txt"
            if os.path.exists(filename):
                text = read_diary(filename)
                audio_filename = text_to_speech(text, filename)
                print("저장된 일기를 재생합니다.")
                play_audio(audio_filename)
            else:
                print("해당 날짜의 일기가 존재하지 않습니다.")
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()