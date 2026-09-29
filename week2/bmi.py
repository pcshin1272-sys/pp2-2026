#
# bmi 계산 함수
# body mass index (bmi) 계산 함수
#

def get_bmi(meight_kg:float, height_m:float) -> float:
    bmi = meight_kg / (height_m/100)**2
    return bmi

def test_bmi() :
    height = 171
    weight = 56
    b = get_bmi(weight, height)
    print(f"키 ({171}) 몸무게 ({56})의 bmi는 {b}입니다.")

if __name__ == "__main__":
    test_bmi()
