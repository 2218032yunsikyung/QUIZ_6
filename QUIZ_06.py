def validate_resident_registration_number(rrn):
    # 입력 주민번호가 숫자가 아니거나 13자리가 아니면 유효하지 않음
    if not rrn.isdigit() or len(rrn) != 13:
        return False

    # 주민번호 뒷자리 숫자
    last_digit = int(rrn[-1])

    # 각 자리에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 곱하여 합산
    weighted_sum = 0
    for i in range(12):
        weighted_sum += int(rrn[i]) * (i % 8 + 2)

    # 합산값을 11로 나눈 나머지를 구하고 11에서 빼줌
    result = 11 - (weighted_sum % 11)

    # 결과 값이 10이면 0으로 처리
    result = result % 10

    # 연산 결과와 주민번호 마지막 자리 숫자를 비교
    if result == last_digit:
        return True
    else:
        return False

num =input("주민등록번호를 입력하세요.")

if validate_resident_registration_number(num):
    print("주민등록번호가 유효합니다.")
else:
    print("주민등록번호가 유효하지 않습니다.")
