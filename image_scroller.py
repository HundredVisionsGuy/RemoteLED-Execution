#!/usr/bin/env python
import time
import datetime
from samplebase import SampleBase
from PIL import Image


class ImageScroller(SampleBase):
    def __init__(self, *args, **kwargs):
        super(ImageScroller, self).__init__(*args, **kwargs)
        self.parser.add_argument("-i", "--image", help="The image to display", default="../../../examples-api-use/runtext.ppm")

    def run(self):
        if not 'image' in self.__dict__:
            self.image = Image.open(self.args.image).convert('RGB')
        self.image.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)

        double_buffer = self.matrix.CreateFrameCanvas()
        img_width, img_height = self.image.size

        # Get minute - to base image on time
        now = datetime.datetime.now()
        minute = now.strftime("%M")
        last_minute = minute
        # let's scroll
        xpos = 0
        switched = False
        while True:
            # get current minute
            minute = now.strftime("%M")
            xpos += 1
            if (xpos > img_width):
                xpos = 0
                # check if a minute has passed
                # if so, it's time to switch images
                if switched:
                    # we can switch picture
                    #print("Minute is {} and last minute was {}".format(minute, last_minute))
                    #if int(minute) % 2 == 0:
                    self.image = Image.open("LEDWelcomeFamily.png").convert('RGB')
                    self.image.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
                    double_buffer = self.matrix.CreateFrameCanvas()
                else:
                        #double_buffer = self.matrix.CreateFrameCanvas()
                        #img_width, img_height = self.image.size
                    #else:
                    self.image = Image.open("LEDWelcomeFamily.png").convert('RGB')
                    self.image.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
                    double_buffer = self.matrix.CreateFrameCanvas()
                switched = not switched
                #double_buffer = self.matrix.CreateFrameCanvas()
                #img_width, img_height = self.image.size

            double_buffer.SetImage(self.image, -xpos)
            double_buffer.SetImage(self.image, -xpos + img_width)

            double_buffer = self.matrix.SwapOnVSync(double_buffer)
            time.sleep(0.01)
            last_minute = minute

# Main function
# e.g. call with
#  sudo ./image-scroller.py --chain=4
# if you have a chain of four
if __name__ == "__main__":
    image_scroller = ImageScroller()
    if (not image_scroller.process()):
        image_scroller.print_help()
