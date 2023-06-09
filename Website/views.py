"""
Here we create the page templates for our webpages.
These templates help us to take care of the requests generated by the webpages.
"""

# Create your views here.
from .forms import ImageForm
from django.shortcuts import render

import numpy as np
from io import BytesIO
import base64
import os
import matplotlib.pyplot as plt
from PIL import Image


import Website.roi_tccc 

cwd = os.getcwd() 
media_dir = os.path.join(os.getcwd(), 'media', 'documents')


def getFileName(path):
    for i in range(len(path) - 1, -1, -1):
        if path[i] == "/" or path[i] == "\\":
            return path[i+1:]


def Image_store(request):
    msg = {
        "message": "Please upload audio.",
        "show": False,
        "where": "start",
        "bgl": -1,
        "lasteat": -1,
    }

    if request.method == 'POST': 
        form = ImageForm(request.POST,request.FILES or None) 
        if form.is_valid(): 
            c = form.save() 
            try:
                # Form Validated
                # leftpath = os.path.join(media_dir, getFileName(str(c.left)))
                leftpath = media_dir + os.sep + getFileName(str(c.left))
                rightpath = media_dir + os.sep + getFileName(str(c.right))
                # rightpath = os.path.join(media_dir, getFileName(str(c.right)))
                print(media_dir)
                print(leftpath)
                print(rightpath)

                tcc_left = tcc_right = None

                try:
                    tcc_left = Website.roi_tccc.main(leftpath)
                except Exception as e:
                    print(e)
                    msg["where"] = "left tcc"
                    
                try:
                    tcc_right = Website.roi_tccc.main(rightpath)
                except Exception as e:
                    print(e)
                    msg["where"] = "right tcc"

                

                msg["lasteat"] = c.lasteat
                lasteat = int(c.lasteat)

                # Convert the figure to web-readble format.
                # buffer = BytesIO()
                # plt.savefig(buffer, format='png')
                # buffer.seek(0)
                # image_png = buffer.getvalue()
                # buffer.close()

                # graphic = base64.b64encode(image_png)
                # graphic = graphic.decode('utf-8')

                # output['waveplot'] = graphic

                offset = 105.857358
                bgl = (0.65600544 * (tcc_left + tcc_right) / 2) - (0.1057725 * lasteat) + offset
                msg['bgl'] = round(bgl)
                msg["where"] = "completed"

            except:
                # Form Invalidated
                return render(request, "upload.html", msg)


            msg['message'] = "Please wait for the prediction to load..."
            msg['show'] = True
            return render(request, "upload.html", msg)

    else: 
        # When the request method is not POST
        form = ImageForm() 
        msg['form'] = form
    return render(request, 'upload.html', msg)


def homePage(request):
    """
    This template handles the requests generated by the home page of the website.
    """

    return render(request, "home.html", {})


def record(request):
    """
    This template handles the requests generated by record page.
    """

    return render(request, "record.html", {"message": "Record the audio and download it in .wav format."})


def about(request):
    """
    This template handles the requests generated by the about page of the website.
    It displays information about the project and links to the resources that were used to create it.
    """
    
    return render(request, "about.html", {})

