#Author- Wenxi Cao / Cici Cao (wenxicao60@gmail.com)

#Reference to：
# Archimedean spiral-https://en.wikipedia.org/wiki/Archimedean_spiral?utm_source
# Daniel Berio-Ndi_numpy_image.py

''''
NDI Sender example using py5canvas and NDIlib
To run you need to install the NDI SDK (system wide) on your machine from:
https://ndi.video/for-developers/ndi-sdk/
And then the ndi-python package with
pip install ndi-python
'''

from py5canvas import *
import NDIlib as ndi

def setup_ndi(name="py5canvas NDI Sender"):
    """ This function initializes NDI for sending video frames once
    If you reload the script, it will not re-initialize NDI and keep the same sender.
    The sender will be exposed as a global `ndi_send` variable
    """
    print("Setting up NDI sender...")
    global ndi_send
    try:
        ndi_send
        return
    except NameError:        
        if not ndi.initialize():
            print("Cannot initialize NDI")

        send_settings = ndi.SendCreate()
        send_settings.ndi_name = name
        ndi_send = ndi.send_create(send_settings)

        
        if ndi_send is None:
            print("Could not initialize NDI sender")


def send_ndi():
    img = get_image().convert('RGBA')
    video_frame = ndi.VideoFrameV2()
    video_frame.data = np.array(img, dtype=np.uint8)
    video_frame.FourCC = ndi.FOURCC_VIDEO_TYPE_RGBA
    ndi.send_send_video_v2(ndi_send, video_frame)


def normalize_image(im):
    return (im - im.min())/(im.max() - im.min())
    

def setup():
    create_canvas(512, 512) #1024, 1024) #512, 512)
    setup_ndi()


def draw():

    background(0)
    
    # Animation
    t = frame_count / 200.0
    
    # Main shaft (vertical line)
    cx = width * 0.5
    cy = height * 0.5
    stroke(255, 120)
    stroke_weight(2)
    line(cx, 0, cx, height)

    # Line Parameters
    N = 900                # Number of Lines
    twist_speed= 0.22 #0.3  
    growth = 0.32       
    x_offset = width * 0.2  # The spiral shifts to the right.
    y_axis = height * 0.95 

    stroke(255, 40)
    stroke_weight(1)

    for i in range(N):
        u = i / (N - 1) #normalization

        # (x0, y0): A point on the main axis
        x0 = cx
        y0 = cy + (u - 0.5) * y_axis

        # (x1, y1): A point on the spiral
        angle = i * twist_speed + t * TWO_PI * 0.6
        r = 6 + i * growth
        
        # Reference to x = r cos(θ)，y = r sin(θ)，
        x1 = cx + cos(angle) * r + x_offset #- x_offset 
        y1 = cy + sin(angle) * r
        
        
        line(x0, y0, x1, y1)

    # Send frame via NDI
    send_ndi()


run()
