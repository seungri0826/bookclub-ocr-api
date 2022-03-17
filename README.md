# 서랍속책방 - OCR 후처리 API
2021-1학기 컴퓨터과학종합설계 - OCR 후처리 API (GCP)

## 설명
`서랍속책방`의 에세이 게시판에서는 책의 인상깊은 구절을 촬영하여 OCR 기능을 이용해 간편하게 텍스트로 변환 후 에세이를 작성할 수 있다. 하지만 Google Cloud Vision API를 통해 OCR로 추출된 텍스트는 페이지에 배치된 모양대로 줄바꿈이 되어있고, 복잡한 모양의 글자의 경우에는 잘못 인식되는 경우가 많다. 이러한 문제점을 보완하기 위해 OCR 후처리 API를 구현하였다.

<br>

## 동작
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a27746b2-5941-4f29-80c7-b49f12054597/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220317T052638Z&X-Amz-Expires=86400&X-Amz-Signature=3913195b159339e9feb591aaae229401d505ba22570e3f208682102a25c9db84&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

<br>

## 구조
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/62632b7c-74cd-4702-848a-74aada5f93b4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220317T052640Z&X-Amz-Expires=86400&X-Amz-Signature=0bae0e1dc8f87aac10655ed98c326d2d9f47c0e0c751375a236e853e51ee7db6&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
