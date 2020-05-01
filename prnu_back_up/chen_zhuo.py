import os
import cv2
import pickle
import numpy as np
from PIL import Image


if __name__ == '__main__':


	candidate_phones = ['贺晓明_vivo_x20',
	                    '雷铁牛_oppo_r9s',
	                    '邓军辉_oppo_a37m',
	                    '陶益安_vivo_x7_plus',
	                    '夏超_iphone_6s_plus']


	if not os.path.exists('候选手机的压缩处理后的图片'):
		os.mkdir('候选手机的压缩处理后的图片')
		for candidate_phone in candidate_phones:
			os.mkdir('候选手机的压缩处理后的图片/{}'.format(candidate_phone))
			for _, _, filenames in os.walk('候选手机的原始未处理的图片/{}'.format(candidate_phone)):
				for filename in filenames:
					extension = filename.split('.')[-1]
					if extension in ['jpg', 'JPG', 'jpeg', 'JPEG']:
						rgb_image = Image.open('候选手机的原始未处理的图片/{}/{}'.format(candidate_phone, filename))
						width, height = rgb_image.size
						if width > height:
							rgb_image = np.rot90(np.array(rgb_image, dtype=np.uint8), k=-1)
							rgb_image = Image.fromarray(rgb_image)
						rgb_image = rgb_image.resize((960, 1280), Image.ANTIALIAS)
						rgb_image.save('候选手机的压缩处理后的图片/{}/{}'.format(candidate_phone, filename), 'jpeg', quality=95)
	

	if not os.path.exists('候选手机的摄像头的PRNU'):
		os.mkdir('候选手机的摄像头的PRNU')
		for candidate_phone in candidate_phones:
			I = []
			W = []
			for _, _, filenames in os.walk('候选手机的压缩处理后的图片/{}'.format(candidate_phone)):
				for filename in filenames:
					extension = filename.split('.')[-1]
					if extension in ['jpg', 'JPG', 'jpeg', 'JPEG']:
						bgr_image = cv2.imread('候选手机的压缩处理后的图片/{}/{}'.format(candidate_phone, filename))
						gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
						gray_image = gray_image[1280//2-400:1280//2+420, 960//2-300:960//2+300]
						i = np.array(gray_image, dtype=np.float64)
						w = i - np.array(cv2.fastNlMeansDenoising(gray_image, None, 10, 7, 21), dtype=np.float64)
						I.append(i)
						W.append(w)
			I = np.array(I, dtype=np.float64)
			W = np.array(W, dtype=np.float64)
			k = np.sum(W * I, axis=0) / np.sum(I * I, axis=0)
			with open('候选手机的摄像头的PRNU/{}'.format(candidate_phone), 'wb') as f:
				pickle.dump(k, f)
	

	for _, _, filenames in os.walk('待溯源的图片'):
		for filename in filenames:
			extension = filename.split('.')[-1]
			if extension in ['jpg', 'JPG', 'jpeg', 'JPEG']:
				bgr_image = cv2.imread('待溯源的图片/{}'.format(filename))
				gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
				gray_image = gray_image[1280//2-400:1280//2+420, 960//2-300:960//2+300]
				i = np.array(gray_image, dtype=np.float64)
				w = i - np.array(cv2.fastNlMeansDenoising(gray_image, None, 10, 7, 21), dtype=np.float64)
				correlation = {}
				for candidate_phone in candidate_phones:
					with open('候选手机的摄像头的PRNU/{}'.format(candidate_phone), 'rb') as f:
						k = pickle.load(f)
					correlation[candidate_phone] = np.sum((w - np.mean(w)) * (k * i - np.mean(k * i))) / (np.sqrt(np.sum((w - np.mean(w)) ** 2)) * np.sqrt(np.sum((k * i - np.mean(k * i)) ** 2)))
				predicted_target_phone = max(correlation, key=correlation.get)
				print('待溯源的图片/{} 最可能来源于 {}'.format(filename, predicted_target_phone))
				for candidate_phone in candidate_phones:
					print('待溯源的图片/{} 与 {} 的相关性为 {:.5f}'.format(filename, candidate_phone, correlation[candidate_phone]))
