# Image manipulation utilities

import cv2
import numpy as np

png_dir = "D:\\Documents\\Projects\\AugRel\\png"


def get_resized_addon(setting, width, height):
    addon_img = ""
    if setting == "unihorn":
        addon_img = cv2.imread(png_dir + "\\unihorn.png", -1)
        # -1 above to load with transparency (alpha channel)

        addon_res = cv2.resize(addon_img, (width, height), interpolation=cv2.INTER_AREA)
        return addon_res

    # TODO: Change these if statements to dictionary switch

    elif setting == "one_devil_horn":
        addon_img = cv2.imread(png_dir + "\\one_devil_horn.png", -1)
        addon_res = cv2.resize(addon_img, (width, height), interpolation=cv2.INTER_AREA)
        return addon_res

    elif setting == "two_horns1":
        addon_img = cv2.imread(png_dir + "\\two_horns1.png", -1)
        addon_res = cv2.resize(addon_img, (width, height), interpolation=cv2.INTER_AREA)
        return addon_res

    elif setting == "two_horns2":
        addon_img = cv2.imread(png_dir + "\\two_horns2.png", -1)
        addon_res = cv2.resize(addon_img, (width, height), interpolation=cv2.INTER_AREA)
        return addon_res

    elif setting == "bunny_ears1":
        addon_img = cv2.imread(png_dir + "\\bunny_ears1.png", -1)
        addon_res = cv2.resize(addon_img, (width, height), interpolation=cv2.INTER_AREA)
        return addon_res

    elif setting == "bunny_ears2":
        addon_img = cv2.imread(png_dir + "\\bunny_ears2.png", -1)
        addon_res = cv2.resize(addon_img, (width, height), interpolation=cv2.INTER_AREA)
        return addon_res

    elif setting == "bunny_ears3":
        addon_img = cv2.imread(png_dir + "\\bunny_ears3.png", -1)
        addon_res = cv2.resize(addon_img, (width, height), interpolation=cv2.INTER_AREA)
        return addon_res

    elif setting == "puppy":
        addon_img = cv2.imread(png_dir + "\\puppy.png", -1)
        addon_res = cv2.resize(addon_img, (width, height), interpolation=cv2.INTER_AREA)
        return addon_res


def blend(rep_place, addon):
    # to separate alpha and BGR layers
    addon_brg = addon[:, :, :3]  # BRG channels
    addon_alpha = addon[:, :, 3:]  # alpha channel

    # find inverse of addon's alpha channel, that is  the background mask:
    addon_alpha_inv = 255 - addon_alpha

    # The alpha masks are one channel right now
    # let's make them 3 channel so that they can be used as weights for:
    # g(x) = a*f1(x) + b*f2(x) + c, using addWeighted

    addon_alpha = cv2.cvtColor(addon_alpha, cv2.COLOR_GRAY2BGR)
    addon_alpha_inv = cv2.cvtColor(addon_alpha_inv, cv2.COLOR_GRAY2BGR)

    # map 0 to 255 into 0.0 to 1.0 float values
    # and find the two weighted parts
    rep_part = (rep_place * (1 / 255)) * (addon_alpha_inv * (1 / 255))
    addon_part = (addon_brg * (1 / 255)) * (addon_alpha * (1 / 255))

    # but we want from 8 bit ints from 0 to 255
    return np.uint8(cv2.addWeighted(rep_part, 255.0, addon_part, 255.0, 0.0))


# returns the image having the overlay
def get_with_overlay(img, setting, x, y, w, h):
    if setting == "unihorn":
        _x = x + (3*w)//7
        _y = y - h//3
        width = w//3
        height = h//2

    elif setting == "one_devil_horn":
        _x = x + (3 * w) // 7
        _y = y - h // 3
        width = w // 4
        height = h // 2

    elif setting == "two_horns1":
        _x = x
        _y = y - h // 2
        width = w
        height = h

    elif setting == "two_horns2":
        _x = x
        _y = y - h // 2
        width = w
        height = h

    elif setting == "bunny_ears1":
        _x = x
        _y = y - ((10 * h) // 14)
        width = w
        height = h

    elif setting == "bunny_ears2":
        _x = x
        _y = y - ((10 * h) // 19)
        width = w
        height = int(h * 0.9)

    elif setting == "bunny_ears3":
        _x = x
        _y = y - ((10 * h) // 19)
        width = w
        height = (3 * h) // 5

    elif setting == "puppy":
        _x = x - int(w*0.07)
        _y = y - ((10 * h) // 32)
        width = int(w*1.2)
        height = int(h*1.1)

    # This next part crops the interested part of the cam footage and passes to the blend function
    # as we need the same size for blending

    transformed = blend(img[_y:_y + height, _x:_x + width], get_resized_addon(setting, width, height))
    img[_y:_y + height, _x:_x + width] = transformed

    return img
