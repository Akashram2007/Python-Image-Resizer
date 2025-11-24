from PIL import Image
import os

input_folder = "."      
output_folder = "resized_images"    
new_size = (800, 800)             
output_format = "PNG"              

os.makedirs(output_folder)

for file in os.listdir(input_folder):
    file_path = os.path.join(input_folder, file)

    try:
        with Image.open(file_path) as img:
            resized_img = img.resize(new_size)

            base_name = os.path.splitext(file)[0]
            new_file_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")

            resized_img.save(new_file_path, output_format)
            print(f"Processed: {file}")

    except Exception as e:
        print(f"Skipped {file} - {e}")

print("\nAll images processed successfully!")