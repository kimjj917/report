weight = float(input("몸무게가 몇 kg인가요?=>"))
height = float(input("키가 몇 m인가요?=>"))
BMI = (weight / (height ** 2))


if BMI <= 18.4:
    print("당신의 BMI는 {}입니다. 따라서 당신은 저체중입니다.".format(round(BMI, 6)))

if 18.5 <= BMI <= 22.9:
    print("당신의 BMI는 {}입니다. 따라서 당신은 정상입니다.".format(round(BMI, 6)))

if 23 <= BMI <= 24.9:
    print("당신의 BMI는 {}입니다. 따라서 당신은 비만 전단계 입니다.".format(round(BMI, 6)))

if 25 <= BMI <= 29.9:
    print("당신의 BMI는 {}입니다. 따라서 당신은 1단계 비만 입니다.".format(round(BMI, 6)))

if 30 <= BMI <= 34.9:
    print("당신의 BMI는 {}입니다. 따라서 당신은 2단계 비만 입니다.".format(round(BMI, 6)))

if 35 <= BMI:
    print("당신의 BMI는 {}입니다. 따라서 당신은 3단계 비만 입니다.".format(round(BMI, 6)))

