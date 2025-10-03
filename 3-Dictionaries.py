# Creating dictionaries
model_config = {
    "num_layers": 12,
    "hidden_size": 768,
    "num_heads": 12,
    "dropout": 0.1
}
print(f"Model config: {model_config}")

# Accessing values by key
hidden_size = model_config["hidden_size"]
print(f"Hidden size: {hidden_size}")

# Using .get() method (safer - returns None if key doesn't exist)
batch_size = model_config.get("batch_size", 32)  # 32 is default value
print(f"Batch size: {batch_size}")

# Adding new key-value pairs
model_config["learning_rate"] = 0.001
print(f"Updated config: {model_config}")

# Updating existing values
model_config["dropout"] = 0.2
print(f"New dropout: {model_config['dropout']}")

# Removing items
del model_config["learning_rate"]
print(f"After deletion: {model_config}")

# Checking if key exists
has_dropout = "dropout" in model_config
print(f"Has dropout: {has_dropout}")

# Getting all keys and values
keys = model_config.keys()
values = model_config.values()
print(f"Keys: {list(keys)}")
print(f"Values: {list(values)}")

# Iterating through dictionary
print("\nModel configuration:")
for key, value in model_config.items():
    print(f"  {key}: {value}")

# Nested dictionaries
training_config = {
    "model": {"type": "ViT", "size": "base"},
    "training": {"epochs": 10, "batch_size": 32}
}
model_type = training_config["model"]["type"]
print(f"\nModel type: {model_type}")
