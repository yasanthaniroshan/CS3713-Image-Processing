# Week 05 Lab

This script performs various image processing operations on a grayscale image using OpenCV and Matplotlib. The operations include generating a negative image, increasing brightness, reducing contrast, reducing grey depth, and creating a vertical mirror of the image. The results are displayed in a subplot and saved to the disk.

## Prerequisites

- Python 
- OpenCV
- NumPy
- Matplotlib

## Installation

1. Clone the repository or download the script.
2. Make a venv and Install the required Python packages using pip:

    ```sh
    python3 -m venv .
    pip install -r requirements.txt
    ```

## Usage

1. Place the source image in the `Inputs` directory with the filename format `210436E_SrcImage.jpg`.
2. Run the script:

    ```sh
    python3 main.py
    ```

3. The processed images will be saved in the `Outputs` directory, and a subplot of the images will be displayed and saved as `210436E_SubPlot.jpg`.

## Script Details

### Constants

- `INDEX` : Index Number for the image.
- `CURRENT_DIR` : Current working directory.
- `IMAGE_URL` : Path to the source image.
- `OUTPUT` : Directory to save the output images.
- `GREYSCALE_IMAGE_URL` : Path to save the grayscale image.
- `PLOT_OUTPUT`: Path to save the subplot image.

### Functions

- `get_negative_image(src_image: np.ndarray) -> np.ndarray` - Generates a negative of the input image.
- `increase_brigtness(src_image: np.ndarray, percentage: float) -> np.ndarray` - Increases the brightness of the input image by a given percentage.
- `reduce_contrast(src_image: np.ndarray, low: int, high: int) -> np.ndarray`- Reduces the contrast of the input image.
- `reduce_grey_depth(src_image: np.ndarray, new_grey_depth) -> np.ndarray`- Reduces the grey depth of the input image.
- `vertical_mirror(src_image: np.ndarray) -> np.ndarray`- Creates a vertical mirror of the input image.

### Main Execution

1. The script reads the source image in grayscale mode.
2. Saves the grayscale image.
3. Applies the following transformations:
    - Negative image
    - Increased brightness
    - Reduced contrast
    - Reduced grey depth
    - Vertical mirror
4. Displays the original and transformed images in a subplot.
5. Saves the subplot image.

## Error Handling

- The script handles errors in loading and saving images by printing an error message and exiting the program.

## Example

```sh
python3 main.py
```

This will process the image `210436E_SrcImage.jpg` located in the `Inputs`directory and save the results in the `Outputs` directory.

## License

This project is licensed under the MIT License. See the LICENSE file for details.


