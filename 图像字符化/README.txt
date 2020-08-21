#Theory
In a picture, each pixel has gray scale(between 0 to 255, if it's 8-bits)
So I pick up 16 ASCII characters(['@', '%', '8', '9', '0', '~', '/', '7', '|', '!', '1', ':', '°', '.', "'", ' ']), you can clearly see that `@` has more density than `.` in the same space. Therefor, I use those 16 characters which has roughly different density to represent the pixel gray scale from the picture.


#Input
In the path where the code is, there should be a picture named `test.jpg` as the input of the code.  

As a consideration, the picture resolution may not be too high(else the output might be to large), one character in the output represent one pixel from the input.

#Output
The code extract the groups of pixels with same gray scale out of the picture, and transfer the edges into ASCII characters. If you found that the output txt file looks weird, do adjust the length-width-ratio in the txt-editor you use(because your txt-editor may set the separation between lines too far), if the view in your txt-editor has roughly the same ratio as the original input picture, you should clearly see the edges.