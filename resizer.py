from PIL import Image

def resize_image(width, height ):
    try:
        image = Image.open('cat.png')
    except FileNotFoundError:
        print("Error : No image was found")


    print ( f"Original Size: {image.size}" )
    try:
        resized_image = image.resize((width,height))
        resized_image.save(f'resized-image_{width}x{height}.png' )
        print("Image was resized sucessfully")
    except Exception as e:
        print(f"Error during Resizing and saving: {e}")

try:
    width = int(input("Enter Width: "))
    height = int(input("Enter Height: "))
    resize_image(width,height)
    print(f"Resized Image Size: {width}x{height}")
except ValueError:
    print("Error: Please enter inegers for width and height")