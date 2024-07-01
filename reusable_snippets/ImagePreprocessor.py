from PIL import Image


# def imagePreprocessor(image_path, max_width=850, max_height=650):
#   try:
#     image = Image.open(image_path)
#     width, height = image.size

#     # Calculate new dimensions to maintain aspect ratio
#     new_width = min(width, max_width)
#     new_height = int(height * (new_width / width)) if width > new_width else height

#     # Resize the image
#     resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
#     return resized_image

#     # Save the resized image
#     resized_image.save(output_path)
#   except Exception as e:
#     print(f"Error resizing image: {e}")


def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)
        img = PIL.Image.open(self.img_listing)
        target_width = 850
        target_height = target_width/1.31
        img = img.resize((int(target_width), int(target_height)), PIL.Image.ANTIALIAS)
        img.save(self.img_listing.path, quality=100)
        img.close()
        self.img_listing.close()    