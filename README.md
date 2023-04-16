<H1 align =center>GLU-CAM </H1>
<p align =center>"Assessment of Glucose Level"</p>
<p align="center">
  <img width="200" src="images/Screenshot 2023-04-16 at 12.08.12 PM.png" alt="Material Bread logo">
</p>


Glu-Cam is a web app for measuring blood glucose levels using a noninvasive method and an easy way to monitor blood glucose levels without expense. It uses the change in the curvature of eye veins, i.e., Tortuous Retinal Vasculature, which is a sign of diabetes in a person. We take the eye images of the eyes, extract the ROI, i.e., veins, and calculate the TRV values of both eyes. The glucose level is predicted by the average TRV value and the time of the last meal using an ML model.

# Features - 

1. Easy to Use.
2. Non-invasive, no need of blood droplet.
3. Does not require any separate hardware module.
4. Does not require internet connection.
5. Works with almost all android mobile devices as it was developed for mobile first.


# Technologies used:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) <br />
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) <br />
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) <br />
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) <br />
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white) <br />
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white) <br />
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) <br />

# Proposed Methodology - 
* Diabetes is associated with loss of capillaries.
* People with diabetes have more Tortuous Retinal Vasculature than persons without diabetes.
* This suggests that retinal vascular tortuosity might be an early indicator of diabetes
* Generally diabetes is diagnosed if the Tortuosity measure is more than 1.15






# Apk Demo
 <p align ="center" >
  <img  width="700" src="images/ezgif.com-video-to-gif.gif" alt="Material Bread logo">
  </p>

## Instructions for running the application

Clone the repository:
```zsh
git clone https://github.com/Vinayak2002/Vaak-Bhaavna.git
```

Create a new virtual environment from the yml file:
```zsh
conda env create -f environment.yml
```

Activate the virtual environment :
```zsh
conda activate FinalWebsite
```

Install all required python packages :
```zsh
pip install -r requirements.txt
```

Install the node package:
```zsh
npm install ffmpeg
```

Add the Secret Key in the settings.py file.

Run the application :
```python
python manage.py runserver
```
---

Made with :heart: at IIIT Naya Raipur .
