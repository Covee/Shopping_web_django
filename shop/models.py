from django.db import models


class Items(models.Model):
	title = models.CharField(max_length=30)  #반찬이름
	description = models.TextField()   #간단한 설명
	# kind =   #반찬종류 (ex.찌개, 젓갈, 나물 등등)
	# price =  #가격
	# point =  #적립금
	# exp_date =  #유통기한
	# number = models.   #수량
	# option =   #옵션선택
	# content = models.TextField()   #메인 상품 상세내용


