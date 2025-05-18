import cv2
import numpy as np

def ensure_alpha_channel(image):
    """
    Adds an alpha channel (fully opaque) if the image doesn't have one.
    """
    if image.shape[2] == 3:  # BGR only
        print("Image has 3 channels, adding alpha channel")
        b, g, r = cv2.split(image)
        alpha = np.ones(b.shape, dtype=b.dtype) * 255  # fully opaque
        return cv2.merge((b, g, r, alpha))
    elif image.shape[2] == 4:
        print("Image already has 4 channels")
        return image  # Already has alpha
    else:
        raise ValueError("Unsupported image format")

def decrease_opacity(input_path, alpha_scale=0.5):
    """
    Ensures alpha channel and decreases opacity of a PNG image.
    
    Parameters:
        input_path (str): Path to input image.
        output_path (str): Path to save output image.
        alpha_scale (float): 0.0 (fully transparent) to 1.0 (original opacity).
    """
    # Load image (unchanged to preserve channels)
    image = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)

    if image is None:
        raise FileNotFoundError(f"Image not found: {input_path}")

    # If image has 2D shape, convert to 3-channel grayscale (edge case)
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGRA)
    elif image.shape[2] == 3:
        image = ensure_alpha_channel(image)
    elif image.shape[2] != 4:
        raise ValueError("Unsupported number of channels")

    # Modify alpha channel
    image[:, :, 3] = np.clip(image[:, :, 3] * alpha_scale, 0, 255).astype(np.uint8)

    return image
    # Save result
    #cv2.imwrite(output_path, image)
    #print(f"Saved image with reduced opacity to {output_path}")

# Example usage
image = decrease_opacity("example.png", alpha_scale=0.1)
image = cv2.resize(image, (0, 0), fx=0.1, fy=0.1)
cv2.imshow("Image with Reduced Opacity", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
