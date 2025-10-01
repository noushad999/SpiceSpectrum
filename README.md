# SpiceSpectrum

#  SpiceSpectrum: Image Preprocessing for Spice Dataset

<img width="1083" height="647" alt="image" src="https://github.com/user-attachments/assets/49eed79d-a246-4dce-bd74-5f45bd014660" />


This repository contains an automated image preprocessing  designed for the **SpiceSpectrum** dataset — a collection of **11,000 images** across **11 different spice categories**. The pipeline prepares raw image data for use in tasks such as **image classification** or **SPICE variety classification.**
dataset and image metadata available at:
https://data.mendeley.com/datasets/5v7w2hx8n5/2

Paper available at:
https://www.sciencedirect.com/science/article/pii/S2352340925008194

---

##  Dataset Overview

- **Total Images:** 11,000
- **Spice Categories:** 11 types (e.g., Turmeric, Coriander, Cumin, etc.)
- **Structure:** Images are organized into folders by spice type.

---

##  Features

 **Square Cropping**  
Automatically crops each image to the largest centered square.

 **Image Resizing**  
Resizes images to a uniform size (either 256×256 or 512×512 pixels).

 **Format Support**  
Supports `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, and `.tiff`.

 **Folder Structure Preservation**  
Maintains the original subfolder hierarchy when saving processed images.

 **Error Handling**  
Skips unreadable or corrupted image files and logs them.

 **Visualization**  
Displays side-by-side visual comparison of original vs. processed images using `matplotlib`.

---

##  Usage

### 1. Clone the Repository
```bash
git clone https://github.com/noushad999/spicespectrum.git
cd spicespectrum
````

### 2. Install Dependencies

```bash
pip install pillow matplotlib
```

### 3. Run the Script

```bash
python foldername.py
```

### 4. Provide Inputs When Prompted:

*  **Output Directory:** Where processed images should be saved.
*  **Target Size:** Enter `256` or `512` for resizing.

---

##  Directory Structure

```
SpiceSpectrum/
├── Turmeric/
│   ├── Turmeric1.jpg
│   └── ...
├── Cumin/
│   └── ...
└── ...
```



##  Use Case

This preprocessing pipeline is designed for:
* Ensuring input uniformity for SPICE metric evaluation
* Cleaning and standardizing datasets for spice classification or recognition systems

---

##  License

This project is licensed under the [MIT License](LICENSE).

---

##  Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve functionality, add features, or fix bugs.

---

##  Contact

For questions or collaborations, please contact:
**\[Md Noushad Jahan Ramim]**
📧 [Noor Mairukh Khan Arnob](mailto:arnob@uap-bd.edu)
📧 [Md Mubtasim Fuad](mailto:mft.turzo@gmail.com)
📧 [contactwithnoushad@gmail.com](mailto:contactwithnoushad@gmail.com)

If you use ideas from our work useful, please cite our paper

```
@article{ramim2025spicespectrum,
  title={SpiceSpectrum: Class-balanced Dataset of Commercially Valuable Spice Cultivars},
  author={Ramim, Md Noushad Jahan and Islam, Samira and Towkir, Muhtasin and Fuad, Md Mubtasim and Arnob, Noor Mairukh Khan},
  journal={Data in Brief},
  pages={112097},
  year={2025},
  publisher={Elsevier}
}
```





