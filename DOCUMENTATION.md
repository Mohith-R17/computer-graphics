```markdown
<div align="center">

# computer-graphics

> A powerful development tool for implementing fundamental Computer Graphics algorithms using Python and OpenGL.

![Language](https://img.shields.io/badge/Python-blue?style=for-the-badge)
![GitHub Stars](https://img.shields.io/github/stars/Mohith-R17/computer-graphics?style=for-the-badge)

</div>

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Tech Stack](#️-tech-stack)
- [Contributing](#-contributing)

---

## 🎯 Overview
This repository presents a comprehensive implementation of core Computer Graphics algorithms built with Python and OpenGL. The project provides efficient, real-time rendering of geometric primitives including Bresenham's line and circle drawing algorithms, the DDA (Digital Differential Analyzer) line algorithm, and the midpoint circle algorithm. Each module leverages modern OpenGL capabilities to generate visual outputs, demonstrating practical applications of discrete mathematics in graphical computing. The codebase serves as both an educational resource and a functional toolkit for developers seeking to implement low-level graphics rendering.

---

## ✨ Features
- 🔷 **Bresenham Line Drawing** – Integer-based algorithm for rendering straight lines without floating-point operations
- 🔷 **Bresenham Circle Drawing** – Efficient generation of circular contours using symmetry optimizations
- 🔷 **DDA Line Drawing** – Digital Differential Analyzer approach for precise line interpolation
- 🔷 **Midpoint Circle Algorithm** – Quarter-circle optimization for faster circle rendering
- 🔷 **Modern OpenGL Integration** – Utilizes `glOrtho`, shaders, and immediate mode for real-time visualization
- 🔷 **Modular Architecture** – Cleanly separated modules for each algorithm with dedicated test cases
- 🔷 **Visual Output Generation** – Automatically produces PNG images of rendered results
- 🔷 **Cross-Platform Compatibility** – Runs consistently across Windows, macOS, and Linux

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- GLFW 2.10.2
- PyOpenGL 3.1.10
- PyOpenGL-accelerate 3.1.10
- NumPy 2.5.1
- Pillow 12.3.0

### Installation
```bash
pip install -r requirements.txt
```

### Quick Start
To view the Bresenham line drawing algorithm:
```bash
python bresenham_line/bresenham_line.py
```

To visualize the Bresenhem circle drawing algorithm:
```bash
python bresenham_circle/bresenham_circle.py
```

To see the DDA line drawing algorithm:
```bash
python dda_line/dda_line.py
```

To explore the midpoint circle algorithm:
```bash
python midpoint_circle/midpoint_circle.py
```

To examine 2D transformations:
```bash
python transformations/transformations.py
```

---

## 📖 Usage

The project consists of four primary algorithm implementations, each accessible via its own script:

**Bresenham Line Drawing**
Renders straight lines between two points using the optimized integer-only Bresenham algorithm. The line color can be customized during execution.

**Bresenham Circle Drawing**
Generates circular contours by plotting eight octants around the center point, leveraging symmetry to minimize computation.

**DDA Line Drawing**
Implements the Digital Differential Analyzer method for drawing lines with high precision, suitable for scenarios requiring sub-pixel accuracy.

**Midpoint Circle Drawing**
Utilizes the midpoint strategy for quarter-circle calculation, which reduces computational complexity compared to full-circle approaches.

All scripts include automatic window management, event polling, and real-time clearing to ensure smooth rendering performance.

---

## 📁 Project Structure
```
computer-graphics/
│
├── bresenham_line/
│   ├── bresenham_line.py      # Bresenham line drawing implementation
│   └── bresenham_line.png     # Generated output image
│
├── bresenham_circle/
│   ├── bresenham_circle.py    # Bresenham circle drawing implementation
│   └── bresenham_circle.png  # Generated output image
│
├── dda_line/
│   ├── dda_line.py           # DDA line drawing implementation
│   └── dda_line.png          # Generated output image
│
├── midpoint_circle/
│   ├── midpoint_circle.py    # Midpoint circle drawing implementation
│   └──                     # (No generated image file present)
│
└── transformations/
    ├── transformations.py    # 2D transformation matrix utilities
```

---

## 🛠️ Tech Stack
| Technology | Version | Purpose |
|------------|---------|----------|
| Python | 3.7+ | Core programming language |
| PyOpenGL | 3.1.10 | GPU-accelerated OpenGL bindings |
| PyOpenGL-accelerate | 3.1.10 | Performance optimizations for OpenGL |
| GLFW | 2.10.2 | Cross-platform window creation and input handling |
| NumPy | 2.5.1 | Numerical computations and array handling |
| Pillow | 12.3.0 | Image processing and export |

---

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure all new code includes appropriate docstrings and follows the existing code style. Test each module thoroughly before submitting updates.
```

```
---

## ⚠️ Documentation Drift Detected

> The README was modified to remove the Midpoint Circle Drawing Algorithm from its table, but the corresponding code file (midpoint_circle/midpoint_circle.py) still exists in the repository, meaning the documentation is outdated.

*This documentation was auto-regenerated by LiveDocAI to reflect the latest code changes.*

---