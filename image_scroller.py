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
        while True:
            # get current minute
            minute = now.strftime("%M")
            xpos += 1
            if (xpos > img_width):
                xpos = 0
                # check if a minute has passed
                # if so, it's time to switch images
                if minute > last_minute or minute == "0":
                    # we can switch picture
                    if int(minute) % 2 == 0:
                        self.image = "you_got_this.png"
                    else:
                        self.image = "LEDWelcomeFamily.png"

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
