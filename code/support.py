from os import walk
import pygame

import pygame
import os

def import_folder(path):
    surface_list = []

    # check if path exists
    if not os.path.exists(path):
        print(f"⚠️ Path not found: {path}")
        return surface_list

    # walk through folder and load images
    for _, __, img_files in os.walk(path):
        for image in img_files:
            if image.lower().endswith((".png", ".jpg", ".jpeg")):
                full_path = os.path.join(path, image)
                try:
                    image_surf = pygame.image.load(full_path).convert_alpha()
                    surface_list.append(image_surf)
                except Exception as e:
                    print(f"⚠️ Failed to load {full_path}: {e}")

    if not surface_list:
        print(f"⚠️ No images found in {path}")

    return surface_list

def import_folder_dict(path):
	surface_dict = {}

	for _, __, img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_dict[image.split('.')[0]] = image_surf

	return surface_dict