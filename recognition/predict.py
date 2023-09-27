from modules import get_maskrcnn_model
import torch
from PIL import Image
from torchvision.transforms import transforms

model = get_maskrcnn_model(num_classes=2)

# Add your path to the saved model here
path_to_saved_model = 'C:\\Users\\yangj\\Desktop\\COMP3710 Project\\Save_Model'
model.load_state_dict(torch.load(path_to_saved_model))
model.eval()

# Load an image and make predictions
path_to_image = 'C:\\Users\\yangj\\Desktop\\COMP3710 Project\\ISIC-2017_Training_Data'
image = Image.open(path_to_image).convert("RGB")
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
])
image = transform(image).unsqueeze(0)
with torch.no_grad():
    predictions = model(image)

# Print results or visualize predictions
print(predictions)
