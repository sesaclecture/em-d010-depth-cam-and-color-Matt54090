import cv2
import numpy as np


# 문제 1.
#
# BGR 이미지를 HSV 이미지로 변환하세요.
#
# OpenCV 함수를 활용하세요.
def convert_to_hsv(image):
    # cv2.cvtColor: 색 공간을 바꾸는 OpenCV 함수
    # 입력이 (H, W, 3)이면 출력도 (H, W, 3)
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


# 문제 2.
#
# BGR 이미지를 LAB 이미지로 변환하세요.
#
# OpenCV 함수를 활용하세요.
def convert_to_lab(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2LAB)


# 문제 3.
#
# 지정한 채널의 평균값을 계산하세요.
#
# channel_index는 사용할 채널 번호입니다.
#
# 예시
# BGR
# 0 -> B
# 1 -> G
# 2 -> R
#
# HSV
# 0 -> H
# 1 -> S
# 2 -> V
#
# LAB
# 0 -> L
# 1 -> A
# 2 -> B
#
# image는 (H, W, 3) 3차원 배열 = (모든 행, 모든 열, 원하는 채널만)
def calculate_channel_mean(
    image,
    channel_index,
):
    channel = image[:, :, channel_index]
    #.mean() : 평균 구하기
    return channel.mean()


# 문제 4.
#
# Color Mask를 생성하세요.
#
# image는 HSV 또는 LAB 이미지입니다.
#
# lower와 upper는 각각
# 색상 범위의 하한과 상한입니다.
#
# OpenCV 함수를 활용하세요.
def create_color_mask(
    image,
    lower,
    upper,
):
    # cv2.inRange: 각각 픽셀들이 [lower, upper] 범위 안에 있는지 검사
    # 픽셀의 모든 채널이 범위 안에 -> 255(흰색)
    # 하나라도 범위 밖이면 -> 0(검은색)
    # 반환은 (H, W) 2차원 흑백 마스크 -> 채널 차원이 None
    return cv2.inRange(image, lower, upper)

# 문제 5.
#
# Binary Mask에서 활성 픽셀 개수를 계산하세요.
#
# 활성 픽셀은 값이 255인 픽셀입니다.
#
# 반환값은 픽셀 개수입니다.
def count_mask_pixels(mask):
    # (mask == 255): 각 픽셀이 255인지 검사 -> True/False 배열.
    # numpy에서 True=1, False=0 이라, sum()을 하면 255인 픽셀 수가 총합
    return (mask == 255).sum()