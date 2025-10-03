# Basic function definition
def calculate_patches(image_size, patch_size):
    """Calculate number of patches in an image."""
    num_patches = (image_size ** 2) // (patch_size ** 2)
    return num_patches

result = calculate_patches(224, 16)
print(f"Number of patches: {result}")

# Function with default parameters
def create_layer(input_size, output_size=768, dropout=0.1):
    """Create a layer configuration with default values."""
    config = {
        "input": input_size,
        "output": output_size,
        "dropout": dropout
    }
    return config

# Using default values
layer1 = create_layer(512)
print(f"Layer with defaults: {layer1}")

# Overriding defaults
layer2 = create_layer(512, output_size=1024, dropout=0.2)
print(f"Layer with custom values: {layer2}")

# Multiple return values
def get_image_info(height, width, channels):
    """Return multiple values about an image."""
    total_pixels = height * width
    size_str = f"{height}x{width}"
    return total_pixels, size_str, channels

pixels, size, ch = get_image_info(224, 224, 3)
print(f"Pixels: {pixels}, Size: {size}, Channels: {ch}")

# Function with type hints (optional but helpful)
def normalize_value(value: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
    """Normalize a value between min and max."""
    return (value - min_val) / (max_val - min_val)

normalized = normalize_value(128, 0, 255)
print(f"Normalized value: {normalized:.3f}")

# Functions calling other functions
def prepare_model_config(num_classes):
    """Prepare a complete model configuration."""
    num_patches = calculate_patches(224, 16)
    config = create_layer(num_patches, output_size=num_classes)
    return config

model_config = prepare_model_config(num_classes=3)
print(f"Model config: {model_config}")
