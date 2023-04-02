# Image-Steganography-Cyber-Security-Project
3rd Semester Project for Cyber Security Students , Colleges and Schools Projects. #hacklife #cybersecurityprojects #hacking#projects



# 📷 Image Steganography 🔒

A tool for hiding secrets in image files 🙊

# Features 🎉

Supports hiding text messages in images 💬

Uses Least Significant Bit (LSB) steganography method 💻

Provides both encoding and decoding functionality 🔄

Easy-to-use IDE interface 📱

# Usage 💡

Clone the repository: git clone https://github.com/bennetbvarghese/ImageSteganography.git 💾

Navigate to the project directory: cd ImageSteganography 🚶‍♂️

Install the required dependencies: pip install -r requirements.txt 🔧

Run the project: python main.py 🚀

# Algorithms and Techniques 🧠

The project uses the **_Least Significant Bit (LSB)_** steganography technique 💻 to hide data in image files 📷. The LSB method works by modifying the least significant bit of the pixel values in an image to encode the hidden data 🤫.

Each pixel in an image is represented by a number, and this number is usually stored in 24 bits or 8 bits per color channel (red, green, and blue). 🟥The LSB technique modifies the least significant bit of each color channel to store the hidden data. For example, if the original pixel value is 10010110, 🟩the least significant bit is 0. 🟦The LSB technique would change this value to 10010111, which would slightly alter the pixel color, but not noticeably to the human eye 👁️. This process is repeated for each pixel in the image, allowing a large amount of hidden data to be stored within the image file 🖼️💾.

The 🔢 **_MD5Sum_** algorithm is a widely used hash function that is commonly used to verify the integrity of a file. In the context of image steganography, it can be used to check the integrity of the image file before and after the hidden data has been encoded 🔍.

The 🔒 **_Advanced Encryption Standard (AES)_** is a widely used symmetric encryption algorithm that can be used in image steganography to secure the hidden data. The AES algorithm uses a symmetric key to both encrypt and decrypt the data, meaning the same key is used for both the encoding and decoding processes 🔑🔓.
# Dependencies 📚

Python 3 🐍

Kali Linux 🐉

Visual Studio Code 💻

Prevent 🎗️

# Limitations ❗️

The maximum size of the hidden data is limited by the size of the image file 📂

The quality of the image may be slightly degraded after encoding 💻

The encoded data may be vulnerable to steganalysis techniques 🔍

# Contributing 🤝

We welcome contributions to the project! If you find a bug or have a feature request, please open an issue on GitHub 💬. If you would like to contribute code, please fork the repository and submit a pull request 💻.

# License 📜

The project is released under the MIT License 🙌. Feel free to use and modify the code for your own projects.
