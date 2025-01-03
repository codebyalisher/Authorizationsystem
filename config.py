import imagekitio

def upload_image_to_imagekit(image_file):
    imagekit = imagekitio.ImageKit(
        private_key="your_private_key",
        public_key="your_public_key",
        url_endpoint="https://ik.imagekit.io/your_imagekit_id"
    )

    upload_response = imagekit.upload_file(
        file=image_file,
        file_name="profile_image.jpg",
        use_unique_file_name=True
    )

    return upload_response['url']
