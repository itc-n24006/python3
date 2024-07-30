a = [
        ['0001', 'Male', 'Yamada', 'Tarou', '25', 'Tokyo'],
        ['0002', 'Male', 'Satou', 'Takeshi', '27', 'Kanagawa'],
        ['0003', 'Female', 'Tanaka', 'Yuko', '25', 'Saitama'],
        ['0004', 'Male', 'Suzuki', 'Ichirou', '35', 'Hokkaido'],
        ]
b = {i[0]: i[1:] for i in a}
for key, info in b.items():
    print(key,info)
