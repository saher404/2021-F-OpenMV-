# Template Matching Example - Normalized Cross Correlation (NCC)
#
# This example shows off how to use the NCC feature of your OpenMV Cam to match
# image patches to parts of an image... expect for extremely controlled enviorments
# NCC is not all to useful.
#
# WARNING: NCC supports needs to be reworked! As of right now this feature needs
# a lot of work to be made into somethin useful. This script will reamin to show
# that the functionality exists, but, in its current state is inadequate.

import time, sensor, image,ustruct
from pyb import UART,LED
from image import SEARCH_EX, SEARCH_DS
#从imgae模块引入SEARCH_EX和SEARCH_DS。使用from import仅仅引入SEARCH_EX,
#SEARCH_DS两个需要的部分，而不把image模块全部引入。

# Reset sensor
sensor.reset()

# Set sensor settings
sensor.set_contrast(1)
sensor.set_gainceiling(16)
# Max resolution for template matching with SEARCH_EX is QQVGA
sensor.set_framesize(sensor.QQVGA)
# You can set windowing to reduce the search image.
#sensor.set_windowing(((640-80)//2, (480-60)//2, 80, 60))
sensor.set_pixformat(sensor.GRAYSCALE)


LED(1).on()
LED(2).on()
LED(3).on()
# Load template.
# Template should be a small (eg. 32x32 pixels) grayscale image.
template1 = image.Image("/1.pgm")
template2 = image.Image("/2.pgm")
templates3 = ["/3.pgm","/3_1.pgm","/3_2.pgm","/3_3.pgm","/3_4.pgm","/3_5.pgm","/3_6.pgm","/3_7.pgm","/3_8.pgm"]
templates4 = ["/4.pgm","/4_1.pgm","/4_2.pgm","/4_3.pgm","/4_4.pgm","/4_5.pgm","/4_6.pgm","/4_7.pgm","/4_8.pgm"]
templates5 = ["/5.pgm","/5_1.pgm","/5_2.pgm","/5_3.pgm","/5_4.pgm","/5_5.pgm","/5_6.pgm","/5_7.pgm","/5_8.pgm"]
templates6 = ["/6.pgm","/6_1.pgm","/6_2.pgm","/6_3.pgm","/6_4.pgm","/6_5.pgm","/6_6.pgm","/6_7.pgm","/6_8.pgm"]
templates7 = ["/7.pgm","/7_1.pgm","/7_2.pgm","/7_3.pgm","/7_4.pgm","/7_5.pgm","/7_6.pgm","/7_7.pgm","/7_8.pgm"]
templates8 = ["/8.pgm","/8_1.pgm","/8_2.pgm","/8_3.pgm","/8_4.pgm","/8_5.pgm","/8_6.pgm","/8_7.pgm","/8_8.pgm"]
#加载模板图片

clock = time.clock()
uart = UART(3,115200)   #定义串口3变量
uart.init(115200, bits=8, parity=None, stop=1) # init with given parameters

def outuart(x,num):
    global uart
    #frame=[0x2C,18,cx%0xff,int(cx/0xff),cy%0xff,int(cy/0xff),0x5B];
    #data = bytearray(frame)
    data = ustruct.pack("<bbhhhhb",      #格式为俩个字符俩个短整型(2字节)
                   0x2C,                      #帧头1
                   0x12,                      #帧头2
                   int(x), # up sample by 4   #数据1
                   int(num), # up sample by 4    #数据2
                   int(0), # up sample by 4    #数据1
                   int(0), # up sample by 4    #数据2
                   0x5B)
    for x in range(5):
        uart.write(data)#必须要传入一个字节数组
        time.sleep_ms(1)
        print(num)

# Run template matching
while (True):
    clock.tick()
    img = sensor.snapshot()
    num=0
    # find_template(template, threshold, [roi, step, search])
    # ROI: The region of interest tuple (x, y, w, h).
    # Step: The loop step used (y+=step, x+=step) use a bigger step to make it faster.
    # Search is either image.SEARCH_EX for exhaustive search or image.SEARCH_DS for diamond search
    #
    # Note1: ROI has to be smaller than the image and bigger than the template.
    # Note2: In diamond search, step and ROI are both ignored.
    r = img.find_template(template1, 0.70, step=5, search=SEARCH_EX) #, roi=(10, 0, 60, 60))
    #find_template(template, threshold, [roi, step, search]),threshold中
    #的0.7是相似度阈值,roi是进行匹配的区域（左上顶点为（10，0），长80宽60的矩形），
    #注意roi的大小要比模板图片大，比frambuffer小。
    #把匹配到的图像标记出来
    if r:
        print(r)
        #img.draw_rectangle(r)
        print('1')
        num=1
        outuart(0,num)
        for x in range(5):
            LED(1).on()
            LED(2).off()
            LED(3).off()
            time.sleep_ms(100)
            LED(1).on()
            LED(2).on()
            LED(3).on()
            time.sleep_ms(100)

    r2_0 = img.find_template(template2, 0.70, step=5, search=SEARCH_EX)
    if r2_0:
        print(r2_0)
        #img.draw_rectangle(r1_3)
        print('2')
        num=2
        outuart(0,num)
        for x in range(5):
            LED(1).on()
            LED(2).off()
            LED(3).off()
            time.sleep_ms(100)
            LED(1).on()
            LED(2).on()
            LED(3).on()
            time.sleep_ms(100)

    r3_0 = img.find_template(image.Image(templates3[0]), 0.70, step=5, search=SEARCH_EX)
    if r3_0:
        print(r3_0)
        #img.draw_rectangle(r1_1)
        print('3')
        num=3
        outuart(0,num)
        for x in range(5):
            LED(1).on()
            LED(2).off()
            LED(3).off()
            time.sleep_ms(100)
            LED(1).on()
            LED(2).on()
            LED(3).on()
            time.sleep_ms(100)

    r4_0 = img.find_template(image.Image(templates4[0]), 0.70, step=5, search=SEARCH_EX)
    if r4_0:
        print(r4_0)
        #img.draw_rectangle(r1_1)
        print('4')
        num=4
        outuart(0,num)
        for x in range(5):
            LED(1).on()
            LED(2).off()
            LED(3).off()
            time.sleep_ms(100)
            LED(1).on()
            LED(2).on()
            LED(3).on()
            time.sleep_ms(100)
    r5_0 = img.find_template(image.Image(templates5[0]), 0.70, step=5, search=SEARCH_EX)
    if r5_0:
        print(r5_0)
        #img.draw_rectangle(r1_1)
        print('5')
        num=5
        outuart(0,num)
        for x in range(5):
            LED(1).on()
            LED(2).off()
            LED(3).off()
            time.sleep_ms(100)
            LED(1).on()
            LED(2).on()
            LED(3).on()
            time.sleep_ms(100)
    r6_0 = img.find_template(image.Image(templates6[0]), 0.70, step=5, search=SEARCH_EX)
    if r6_0:
        print(r6_0)
        #img.draw_rectangle(r1_1)
        print('6')
        num=6
        outuart(0,num)
        for x in range(5):
            LED(1).on()
            LED(2).off()
            LED(3).off()
            time.sleep_ms(100)
            LED(1).on()
            LED(2).on()
            LED(3).on()
            time.sleep_ms(100)
    r7_0 = img.find_template(image.Image(templates7[0]), 0.70, step=5, search=SEARCH_EX)
    if r7_0:
        print(r7_0)
        #img.draw_rectangle(r1_1)
        print('7')
        num=7
        outuart(0,num)
        for x in range(5):
            LED(1).on()
            LED(2).off()
            LED(3).off()
            time.sleep_ms(100)
            LED(1).on()
            LED(2).on()
            LED(3).on()
            time.sleep_ms(100)
    r8_0 = img.find_template(image.Image(templates8[0]), 0.70, step=5, search=SEARCH_EX)
    if r8_0:
        print(r8_0)
        #img.draw_rectangle(r1_1)
        print('8')
        num=8
        outuart(0,num)
        for x in range(5):
            LED(1).on()
            LED(2).off()
            LED(3).off()
            time.sleep_ms(100)
            LED(1).on()
            LED(2).on()
            LED(3).on()
            time.sleep_ms(100)


    if num!=0:
        while(True):
            clock.tick()
            img = sensor.snapshot()
            if num==1:
                outuart(0,num)
            if num==2:
                outuart(0,num)

            if num==3:
                r3_0 = img.find_template(image.Image(templates3[0]), 0.70, step=5, search=SEARCH_EX)
                if r3_0:
                    print(r3_0)
                    #img.draw_rectangle(r1_1)
                    print('3')
                    outuart(r3_0[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_1 = img.find_template(image.Image(templates3[1]), 0.70, step=5, search=SEARCH_EX)
                if r3_1:
                    print(r3_1)
                    #img.draw_rectangle(r1_1)
                    print('3')
                    outuart(r3_1[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_2 = img.find_template(image.Image(templates3[2]), 0.70, step=5, search=SEARCH_EX)
                if r3_2:
                    print(r3_2)
                    #img.draw_rectangle(r1_2)
                    print('3')
                    outuart(r3_2[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_3 = img.find_template(image.Image(templates3[3]), 0.70, step=5, search=SEARCH_EX)
                if r3_3:
                    print(r3_3)
                    #img.draw_rectangle(r1_2)
                    print('3')
                    outuart(r3_3[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_4 = img.find_template(image.Image(templates3[4]), 0.70, step=5, search=SEARCH_EX)
                if r3_4:
                    print(r3_4)
                    #img.draw_rectangle(r1_2)
                    print('3')
                    outuart(r3_4[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_5 = img.find_template(image.Image(templates3[5]), 0.70, step=5, search=SEARCH_EX)
                if r3_5:
                    print(r3_5)
                    #img.draw_rectangle(r1_2)
                    print('3')
                    outuart(r3_5[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_6 = img.find_template(image.Image(templates3[6]), 0.70, step=5, search=SEARCH_EX)
                if r3_6:
                    print(r3_6)
                    #img.draw_rectangle(r1_2)
                    print('3')
                    outuart(r3_6[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_7 = img.find_template(image.Image(templates3[7]), 0.70, step=5, search=SEARCH_EX)
                if r3_7:
                    print(r3_7)
                    #img.draw_rectangle(r1_2)
                    print('3')
                    outuart(r3_7[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r3_8 = img.find_template(image.Image(templates3[8]), 0.70, step=5, search=SEARCH_EX)
                if r3_8:
                    print(r3_8)
                    #img.draw_rectangle(r1_2)
                    print('3')
                    outuart(r3_8[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
            if num==4:
                r4_0 = img.find_template(image.Image(templates4[0]), 0.70, step=5, search=SEARCH_EX)
                if r4_0:
                    print(r4_0)
                    #img.draw_rectangle(r1_1)
                    print('4')
                    outuart(r4_0[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_1 = img.find_template(image.Image(templates4[1]), 0.70, step=5, search=SEARCH_EX)
                if r4_1:
                    print(r4_1)
                    #img.draw_rectangle(r1_1)
                    print('4')
                    outuart(r4_1[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_2 = img.find_template(image.Image(templates4[2]), 0.70, step=5, search=SEARCH_EX)
                if r4_2:
                    print(r4_2)
                    #img.draw_rectangle(r1_2)
                    print('4')
                    outuart(r4_2[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_3 = img.find_template(image.Image(templates4[3]), 0.70, step=5, search=SEARCH_EX)
                if r4_3:
                    print(r4_3)
                    #img.draw_rectangle(r1_2)
                    print('4')
                    outuart(r4_3[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_4 = img.find_template(image.Image(templates4[4]), 0.70, step=5, search=SEARCH_EX)
                if r4_4:
                    print(r4_4)
                    #img.draw_rectangle(r1_2)
                    print('4')
                    outuart(r4_4[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_5 = img.find_template(image.Image(templates4[5]), 0.70, step=5, search=SEARCH_EX)
                if r4_5:
                    print(r4_5)
                    #img.draw_rectangle(r1_2)
                    print('4')
                    outuart(r4_5[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_6 = img.find_template(image.Image(templates4[6]), 0.70, step=5, search=SEARCH_EX)
                if r4_6:
                    print(r4_6)
                    #img.draw_rectangle(r1_2)
                    print('4')
                    outuart(r4_6[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_7 = img.find_template(image.Image(templates4[7]), 0.70, step=5, search=SEARCH_EX)
                if r4_7:
                    print(r4_7)
                    #img.draw_rectangle(r1_2)
                    print('4')
                    outuart(r4_7[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r4_8 = img.find_template(image.Image(templates4[8]), 0.70, step=5, search=SEARCH_EX)
                if r4_8:
                    print(r4_8)
                    #img.draw_rectangle(r1_2)
                    print('4')
                    outuart(r4_8[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
            if num==5:
                r5_0 = img.find_template(image.Image(templates5[0]), 0.70, step=5, search=SEARCH_EX)
                if r5_0:
                    print(r5_0)
                    #img.draw_rectangle(r1_1)
                    print('5')
                    outuart(r5_0[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_1 = img.find_template(image.Image(templates5[1]), 0.70, step=5, search=SEARCH_EX)
                if r5_1:
                    print(r5_1)
                    #img.draw_rectangle(r1_1)
                    print('5')
                    outuart(r5_1[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_2 = img.find_template(image.Image(templates5[2]), 0.70, step=5, search=SEARCH_EX)
                if r5_2:
                    print(r5_2)
                    #img.draw_rectangle(r1_2)
                    print('5')
                    outuart(r5_2[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_3 = img.find_template(image.Image(templates5[3]), 0.70, step=5, search=SEARCH_EX)
                if r5_3:
                    print(r5_3)
                    #img.draw_rectangle(r1_2)
                    print('5')
                    outuart(r5_3[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_4 = img.find_template(image.Image(templates5[4]), 0.70, step=5, search=SEARCH_EX)
                if r5_4:
                    print(r5_4)
                    #img.draw_rectangle(r1_2)
                    print('5')
                    outuart(r5_4[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_5 = img.find_template(image.Image(templates5[5]), 0.70, step=5, search=SEARCH_EX)
                if r5_5:
                    print(r5_5)
                    #img.draw_rectangle(r1_2)
                    print('5')
                    outuart(r5_5[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_6 = img.find_template(image.Image(templates5[6]), 0.70, step=5, search=SEARCH_EX)
                if r5_6:
                    print(r5_6)
                    #img.draw_rectangle(r1_2)
                    print('5')
                    outuart(r5_6[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_7 = img.find_template(image.Image(templates5[7]), 0.70, step=5, search=SEARCH_EX)
                if r5_7:
                    print(r5_7)
                    #img.draw_rectangle(r1_2)
                    print('5')
                    outuart(r5_7[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r5_8 = img.find_template(image.Image(templates5[8]), 0.70, step=5, search=SEARCH_EX)
                if r5_8:
                    print(r5_8)
                    #img.draw_rectangle(r1_2)
                    print('5')
                    outuart(r5_8[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
            if num==6:
                r6_0 = img.find_template(image.Image(templates6[0]), 0.70, step=5, search=SEARCH_EX)
                if r6_0:
                    print(r6_0)
                    #img.draw_rectangle(r1_1)
                    print('6')
                    outuart(r6_0[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_1 = img.find_template(image.Image(templates6[1]), 0.70, step=5, search=SEARCH_EX)
                if r6_1:
                    print(r6_1)
                    #img.draw_rectangle(r1_1)
                    print('6')
                    outuart(r6_1[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_2 = img.find_template(image.Image(templates6[2]), 0.70, step=5, search=SEARCH_EX)
                if r6_2:
                    print(r6_2)
                    #img.draw_rectangle(r1_2)
                    print('6')
                    outuart(r6_2[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_3 = img.find_template(image.Image(templates6[3]), 0.70, step=5, search=SEARCH_EX)
                if r6_3:
                    print(r6_3)
                    #img.draw_rectangle(r1_2)
                    print('6')
                    outuart(r6_3[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_4 = img.find_template(image.Image(templates6[4]), 0.70, step=5, search=SEARCH_EX)
                if r6_4:
                    print(r6_4)
                    #img.draw_rectangle(r1_2)
                    print('6')
                    outuart(r6_4[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_5 = img.find_template(image.Image(templates6[5]), 0.70, step=5, search=SEARCH_EX)
                if r6_5:
                    print(r6_5)
                    #img.draw_rectangle(r1_2)
                    print('6')
                    outuart(r6_5[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_6 = img.find_template(image.Image(templates6[6]), 0.70, step=5, search=SEARCH_EX)
                if r6_6:
                    print(r6_6)
                    #img.draw_rectangle(r1_2)
                    print('6')
                    outuart(r6_6[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_7 = img.find_template(image.Image(templates6[7]), 0.70, step=5, search=SEARCH_EX)
                if r6_7:
                    print(r6_7)
                    #img.draw_rectangle(r1_2)
                    print('6')
                    outuart(r6_7[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r6_8 = img.find_template(image.Image(templates6[8]), 0.70, step=5, search=SEARCH_EX)
                if r6_8:
                    print(r6_8)
                    #img.draw_rectangle(r1_2)
                    print('6')
                    outuart(r6_8[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
            if num==7:
                r7_0 = img.find_template(image.Image(templates7[0]), 0.70, step=5, search=SEARCH_EX)
                if r7_0:
                    print(r7_0)
                    #img.draw_rectangle(r1_1)
                    print('7')
                    outuart(r7_0[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_1 = img.find_template(image.Image(templates7[1]), 0.70, step=5, search=SEARCH_EX)
                if r7_1:
                    print(r7_1)
                    #img.draw_rectangle(r1_1)
                    print('7')
                    outuart(r7_1[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_2 = img.find_template(image.Image(templates7[2]), 0.70, step=5, search=SEARCH_EX)
                if r7_2:
                    print(r7_2)
                    #img.draw_rectangle(r1_2)
                    print('7')
                    outuart(r7_2[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_3 = img.find_template(image.Image(templates7[3]), 0.70, step=5, search=SEARCH_EX)
                if r7_3:
                    print(r7_3)
                    #img.draw_rectangle(r1_2)
                    print('7')
                    outuart(r7_3[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_4 = img.find_template(image.Image(templates7[4]), 0.70, step=5, search=SEARCH_EX)
                if r7_4:
                    print(r7_4)
                    #img.draw_rectangle(r1_2)
                    print('7')
                    outuart(r7_4[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_5 = img.find_template(image.Image(templates7[5]), 0.70, step=5, search=SEARCH_EX)
                if r7_5:
                    print(r7_5)
                    #img.draw_rectangle(r1_2)
                    print('7')
                    outuart(r7_5[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_6 = img.find_template(image.Image(templates7[6]), 0.70, step=5, search=SEARCH_EX)
                if r7_6:
                    print(r7_6)
                    #img.draw_rectangle(r1_2)
                    print('7')
                    outuart(r7_6[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_7 = img.find_template(image.Image(templates7[7]), 0.70, step=5, search=SEARCH_EX)
                if r7_7:
                    print(r7_7)
                    #img.draw_rectangle(r1_2)
                    print('7')
                    outuart(r7_7[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r7_8 = img.find_template(image.Image(templates7[8]), 0.70, step=5, search=SEARCH_EX)
                if r7_8:
                    print(r7_8)
                    #img.draw_rectangle(r1_2)
                    print('7')
                    outuart(r7_8[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
            if num==8:
                r8_0 = img.find_template(image.Image(templates8[0]), 0.70, step=5, search=SEARCH_EX)
                if r8_0:
                    print(r8_0)
                    #img.draw_rectangle(r1_1)
                    print('8')
                    outuart(r8_0[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_1 = img.find_template(image.Image(templates8[1]), 0.70, step=5, search=SEARCH_EX)
                if r8_1:
                    print(r8_1)
                    #img.draw_rectangle(r1_1)
                    print('8')
                    outuart(r8_1[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_2 = img.find_template(image.Image(templates8[2]), 0.70, step=5, search=SEARCH_EX)
                if r8_2:
                    print(r8_2)
                    #img.draw_rectangle(r1_2)
                    print('8')
                    outuart(r8_2[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_3 = img.find_template(image.Image(templates8[3]), 0.70, step=5, search=SEARCH_EX)
                if r8_3:
                    print(r8_3)
                    #img.draw_rectangle(r1_2)
                    print('8')
                    outuart(r8_3[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_4 = img.find_template(image.Image(templates8[4]), 0.70, step=5, search=SEARCH_EX)
                if r8_4:
                    print(r8_4)
                    #img.draw_rectangle(r1_2)
                    print('8')
                    outuart(r8_4[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_5 = img.find_template(image.Image(templates8[5]), 0.70, step=5, search=SEARCH_EX)
                if r8_5:
                    print(r8_5)
                    #img.draw_rectangle(r1_2)
                    print('8')
                    outuart(r8_5[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_6 = img.find_template(image.Image(templates8[6]), 0.70, step=5, search=SEARCH_EX)
                if r8_6:
                    print(r8_6)
                    #img.draw_rectangle(r1_2)
                    print('8')
                    outuart(r8_6[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_7 = img.find_template(image.Image(templates8[7]), 0.70, step=5, search=SEARCH_EX)
                if r8_7:
                    print(r8_7)
                    #img.draw_rectangle(r1_2)
                    print('8')
                    outuart(r8_7[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
                r8_8 = img.find_template(image.Image(templates3[8]), 0.70, step=5, search=SEARCH_EX)
                if r8_8:
                    print(r8_8)
                    #img.draw_rectangle(r1_2)
                    print('8')
                    outuart(r8_8[0],num)
                    for x in range(5):
                        LED(1).on()
                        LED(2).off()
                        LED(3).off()
                        time.sleep_ms(100)
                        LED(1).on()
                        LED(2).on()
                        LED(3).on()
                        time.sleep_ms(100)
            print(clock.fps())
    print(clock.fps())

