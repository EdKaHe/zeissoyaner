img1 = imread('train/BORDERTOUCHER/008_2.tif');

figure(1)
imshow(img1)
figure(2)
imshow(imgaussfilt(img1))