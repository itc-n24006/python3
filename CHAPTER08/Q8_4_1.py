import re

x = 'かなり昔のRX-7で東京駅まで送ってもらい、成田空港からBoeing787で高松空港まで行き、帰り道はN700系で岡山から戻りました。'
print(re.findall(r'[a-zA-Z0-9\-]+', x))

