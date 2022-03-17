# 서랍속책방 - OCR 후처리 API
2021-1학기 컴퓨터과학종합설계 - OCR 후처리 API (GCP)

<br>

## 설명
`서랍속책방`의 에세이 게시판에서는 책의 인상깊은 구절을 촬영하여 OCR 기능을 이용해 간편하게 텍스트로 변환 후 에세이를 작성할 수 있다. 하지만 Google Cloud Vision API를 통해 OCR로 추출된 텍스트는 페이지에 배치된 모양대로 줄바꿈이 되어있고, 복잡한 모양의 글자의 경우에는 잘못 인식되는 경우가 많다. 이러한 문제점을 보완하기 위해 OCR 후처리 API를 구현하였다.

<br>

## 전체 동작
![](https://user-images.githubusercontent.com/43572543/158791260-e159bbb6-2ff0-41e4-a6c7-05717b1a5f17.png)

<br>

## 구조 및 설계
![](https://user-images.githubusercontent.com/43572543/158791291-2952b24b-3776-4f01-a803-ec5fc0ed8c79.png)
