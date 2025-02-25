# Basic Image Steganography

This project demonstrates a simple image steganography technique using OpenCV. It allows users to hide a secret message inside an image and retrieve it later using a passcode.

## Features
- Encrypts a text message inside an image by modifying pixel values.
- Uses a delimiter (`~`) to mark the end of the message.
- Decrypts and retrieves the hidden message from the image.

## Requirements
Make sure you have Python installed along with the required dependencies:
```sh
pip install opencv-python
```

## How to Use

### Encryption
1. Place an image (e.g., `Anime.jpg`) in the project directory.
2. Run the `encryption.py` script:
    ```sh
    python encryption.py
    ```
3. Enter the secret message and a passcode.
4. The encrypted image will be saved as `encryptedImage.png`.

### Decryption
1. Run the `decryption.py` script:
    ```sh
    python decryption.py
    ```
2. Enter the correct passcode.
3. The hidden message will be displayed.

## File Structure
```
├── encryption.py  # Script for embedding the message
├── decryption.py  # Script for extracting the message
├── Anime.jpg      # Original image (provide your own)
├── encryptedImage.png  # Output image after encryption
├── README.md      # Documentation
```

## Notes
- The image must be large enough to store the entire message.
- Ensure the encrypted image (`encryptedImage.png`) exists before running the decryption script.
- This implementation modifies pixel values directly, so encrypted images may appear slightly altered.

## License
This project is open-source and available for educational purposes.
