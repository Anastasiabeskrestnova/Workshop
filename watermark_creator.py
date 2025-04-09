
from PIL import Image

MAIN_IMG_PATH = "/Users/nastyabeskrestnova/Documents/workshop/wide.png"
WATER_MARK_PATH = "/Users/nastyabeskrestnova/Documents/workshop/petryk.png"
WATER_MARK_SIZE = (200,200)

def water_mark_location(water_mark, main_img):
    water_mark, water_mark_height = water_mark.size
    main_img_width, main_img_height =  main_img.size

    return (water_mark - main_img_width, water_mark_height - main_img_height)

try:
    with Image.open(MAIN_IMG_PATH) as main_img, Image.open(WATER_MARK_PATH) as water_mark:
        main_img = main_img.resize(WATER_MARK_SIZE).convert("RGBA")
        main_img.putalpha(125)
        blank_image = Image.new("RGBA", (water_mark.size))
        blank_image.paste(main_img, water_mark_location(water_mark, main_img))
        water_mark_over_img = Image.alpha_composite(water_mark.convert("RGBA"), blank_image) 
        Image.alpha_composite(water_mark.convert("RGBA"), blank_image).save("water_mark_over_img.png").show()
        water_mark_over_img.show()

except IOError:
    print("Either the name of the file or the path is incorrect.")
    pass
