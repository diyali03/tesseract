# Tesseract
## Install On Mac

Follow the offcial installation guid
## First test
### 1 Homebrew is so sweet - brew install tesseract
### 2 Copy chi package to the tessdata dir
### 3 Using tesseract -help to check option 
### 4 Tips

    tesseract --help-psm

    0    Orientation and script detection (OSD) only.
    1    Automatic page segmentation with OSD.
    2    Automatic page segmentation, but no OSD, or OCR.
    3    Fully automatic page segmentation, but no OSD. (Default)
    4    Assume a single column of text of variable sizes.
    5    Assume a single uniform block of vertically aligned text.
    6    Assume a single uniform block of text.
    7    Treat the image as a single text line.
    8    Treat the image as a single word.
    9    Treat the image as a single word in a circle.
    10    Treat the image as a single character.
    翻译（可能不是很准,最好看原文）：
    0 定向脚本监测（OSD）
    1 使用OSD自动分页
    2 自动分页，但是不使用OSD或OCR（Optical Character Recognition，光学字符识别）
    3 全自动分页，但是没有使用OSD（默认）
    4 假设可变大小的一个文本列。
    5 假设垂直对齐文本的单个统一块。
    6 假设一个统一的文本块。
    7 将图像视为单个文本行。
    8 将图像视为单个词。
    9 将图像视为圆中的单个词。
    10 将图像视为单个字符。


## Install on Linux

### Have some error about the libleptonica-dev
can not remove and upgrade the package, so I use 

`sudo apt-get purge runit`

`sudo apt-get purge autoremove`

Then reinstall the whole package again.


Note
===

echo is use to create file and file contants

see http://www.jianshu.com/p/016e55c25521