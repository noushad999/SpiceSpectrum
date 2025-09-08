# SpiceSpectrum

#  SpiceSpectrum: Image Preprocessing for SPICE Dataset

This repository contains an automated image preprocessing  designed for the **SpiceSpectrum** dataset — a collection of **11,000 images** across **11 different spice categories**. The pipeline prepares raw image data for use in tasks such as **image classification** or **SPICE evaluation**

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
📧 [Noor Mairukh Khan Arnob](mailto:arnob39@gmail.com)
📧 [Md Mubtasim Fuad](mailto:mft.turzo@gmail.com)
📧 [contactwithnoushad@gmail.com](mailto:contactwithnoushad@gmail.com)





