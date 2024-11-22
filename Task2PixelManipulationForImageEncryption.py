from PIL import Image
import numpy as np
import os

# Define]ing the paths
original_image_path = 'image/img.png'
encrypted_image_path = 'image/encrypted_img.png'
decrypted_image_path = 'image/decrypted_img.png'

# Checking if the 'image' folder exists
if not os.path.exists('image'):
    print("Error: 'image' folder does not exist.")
    exit()

# Loading the original image
try:
    img = Image.open(original_image_path)
except FileNotFoundError:
    print(f"Error: The file {original_image_path} does not exist.")
    exit()

# Converting image to a numpy array for manipulation
img_data = np.array(img)

# Defining a shift value for encryption and decryption
shift_value = 50

# Encryption: Adding the shift value to the pixel values
encrypted_data = img_data + shift_value
encrypted_data = np.clip(encrypted_data, 0, 255)  # Ensure pixel values are within the valid range (0-255)

# Saving the encrypted image
encrypted_img = Image.fromarray(encrypted_data.astype(np.uint8))
encrypted_img.save(encrypted_image_path)
print(f"Encrypted image saved as {encrypted_image_path}")

# Decryption: Subtracting the shift value to restore the original image
decrypted_data = encrypted_data - shift_value
decrypted_data = np.clip(decrypted_data, 0, 255)  # Ensure pixel values are within the valid range

# Saving the decrypted image
decrypted_img = Image.fromarray(decrypted_data.astype(np.uint8))
decrypted_img.save(decrypted_image_path)
print(f"Decrypted image saved as {decrypted_image_path}")
print("Image encryption and decryption completed successfully!")


