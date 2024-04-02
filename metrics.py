import os

from math import log10, sqrt 
import cv2 
import numpy as np 

from scipy.stats import entropy



def PSNR(original, compressed): 
  mse = np.mean((original - compressed) ** 2) 
  if(mse == 0):  # MSE is zero means no noise is present in the signal . 
                # Therefore PSNR have no importance. 
      return 100
  max_pixel = 255.0
  psnr = 20 * log10(max_pixel / sqrt(mse)) 
  return psnr 


def PSNR_for_dir(source_dir1, source_dir2, destination_file):
  image_names = [file for file in os.listdir(source_dir1) if not file.startswith('.')]
  psnr_scores = []
  for name in image_names:
    image1 = cv2.imread(os.path.join(source_dir1, name))
    image2 = cv2.imread(os.path.join(source_dir2, name))
    psnr = PSNR(image1, image2)
    psnr_scores.append(psnr)
  with open(destination_file, "a") as f:
    for idx, name in enumerate(image_names):
      f.write(f"{name}\t{psnr_scores[idx]}" + "\n")
    avg_score = sum(psnr_scores) / len(psnr_scores)
    f.write(f"\navg_score\t{avg_score}" + "\n")
  return avg_score


def entropy_(image):
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  _bins = 128
  hist, _ = np.histogram(gray_image.ravel(), bins=_bins, range=(0, _bins))
  prob_dist = hist / hist.sum()
  image_entropy = entropy(prob_dist, base=2)
  return image_entropy


def entropy_for_dir(source_dir, destination_file):
  image_names = [file for file in os.listdir(source_dir) if not file.startswith('.')]
  entropy_scores = []
  for name in image_names:
    image = cv2.imread(os.path.join(source_dir, name))
    entr = entropy_(image)
    entropy_scores.append(entr)
  with open(destination_file, "a") as f:
    for idx, name in enumerate(image_names):
      f.write(f"{name}\t{entropy_scores[idx]}" + "\n")
    avg_score = sum(entropy_scores) / len(entropy_scores)
    f.write(f"\navg_score\t{avg_score}" + "\n")
  return avg_score