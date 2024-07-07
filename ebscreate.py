from moviepy.editor import *
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
import os

# Soru ve resimlerin bulunduğu dizinler
questions = [
    {
        "text": """Herkeze İyi Günler Arkadaşlar bu Videomuzda sizlere otomatik video oluşturmayı göstereceğim...""",
        "image_path": "soru1_resmi.jpg"
    }
    # Diğer soruları burada benzer formatta ekleyin
]

# Çıkış dizini
output_dir = "cikti_videolar"
os.makedirs(output_dir, exist_ok=True)

def create_background_with_image(image_path, output_path):
    # Beyaz arka plan oluşturma
    background = Image.new('RGB', (720, 1280), (255, 255, 255))
    
    # Resmi açma
    image = Image.open(image_path)
    image.thumbnail((640, 640))  # Resmi uygun boyutta yeniden boyutlandır
    
    # Resmi ortalama
    bg_w, bg_h = background.size
    img_w, img_h = image.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(image, offset)
    
    # Görseli kaydetme
    background.save(output_path)

def create_audio_from_text(text, output_path):
    # Seslendirme
    tts = gTTS(text=text, lang='tr', slow=False)
    tts.save(output_path)

def create_video(image_path, audio_path, output_path):
    # Görsel ve ses dosyalarını yükleme
    video_clip = ImageClip(image_path).set_duration(10)
    audio_clip = AudioFileClip(audio_path)
    
    # Ses klibini video klip ile birleştirme
    final_clip = video_clip.set_audio(audio_clip)
    
    # Video dosyasını kaydetme
    final_clip.write_videofile(output_path, fps=24)

# İlgili  videoları oluşturma
for i, question in enumerate(questions):
    question_text = question["text"]
    image_path = question["image_path"]
    
    # Dosya yolları
    bg_image_path = f"{output_dir}/background_with_image_{i+1}.jpg"
    audio_path = f"{output_dir}/question_audio_{i+1}.mp3"
    video_path = f"{output_dir}/question_video_{i+1}.mp4"
    
    # Adımları gerçekleştirme
    create_background_with_image(image_path, bg_image_path)
    create_audio_from_text(question_text, audio_path)
    create_video(bg_image_path, audio_path, video_path)
    
    print(f"{i+1}. video oluşturuldu: {video_path}")
