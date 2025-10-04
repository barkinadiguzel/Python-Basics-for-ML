# Basic class definition
class ImageProcessor:
    """A simple image processor class."""
    
    def __init__(self, image_size):
        """
        Initialize the processor with image size.
        __init__ is called when creating a new object.
        """
        self.image_size = image_size  # instance attribute
        self.processed_count = 0
    
    def process(self, image_name):
        """Process an image and increment counter."""
        self.processed_count += 1
        return f"Processed {image_name} at size {self.image_size}"
    
    def get_stats(self):
        """Return processing statistics."""
        return f"Processed {self.processed_count} images"

# Creating an object (instance) of the class
processor = ImageProcessor(image_size=224)
print(processor.process("cat.jpg"))
print(processor.process("dog.jpg"))
print(processor.get_stats())

# Class with default values
class ModelConfig:
    """Configuration for a neural network model."""
    
    def __init__(self, num_layers=12, hidden_size=768, dropout=0.1):
        self.num_layers = num_layers
        self.hidden_size = hidden_size
        self.dropout = dropout
    
    def display(self):
        """Display current configuration."""
        print(f"Layers: {self.num_layers}")
        print(f"Hidden size: {self.hidden_size}")
        print(f"Dropout: {self.dropout}")

# Create with default values
config1 = ModelConfig()
print("\nDefault config:")
config1.display()

# Create with custom values
config2 = ModelConfig(num_layers=24, hidden_size=1024)
print("\nCustom config:")
config2.display()

# Class inheritance - creating a class based on another
class AdvancedProcessor(ImageProcessor):
    """Extended processor with additional features."""
    
    def __init__(self, image_size, quality="high"):
        super().__init__(image_size)  # call parent's __init__
        self.quality = quality
    
    def process_batch(self, image_names):
        """Process multiple images at once."""
        results = []
        for name in image_names:
            result = self.process(name)
            results.append(result)
        return results

# Using the inherited class
advanced = AdvancedProcessor(image_size=512, quality="ultra")
batch_results = advanced.process_batch(["img1.jpg", "img2.jpg"])
print(f"\nBatch processing:")
for result in batch_results:
    print(f"  {result}")
print(advanced.get_stats())
