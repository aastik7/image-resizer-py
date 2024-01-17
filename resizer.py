from PIL import Image

def resize_image(width, height ):
    image = Image.open('cat.png')


    print ( f"Original Size: {image.size}" )

    resized_image = image.resize((width,height))

    resized_image.save(f'resized-image_{width}x{height}.png' )

width = int(input("Enter Width: "))
height = int(input("Enter Height: "))
resize_image(width,height)
print(f"Resized Image Size: {width}x{height}")