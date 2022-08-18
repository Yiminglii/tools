import torchvision.transforms as transforms
import os

class trans():
    def __init__(self) -> None:
        pass
    def img_to_tensor(img):
        fc=transforms.ToTensor()
        tensor=fc(img)
        tensor=tensor.unsqueeze(0)
        return tensor
    
    def tensor_to_img(tensor):
        fc=transforms.ToPILImage()
        img=tensor.cpu().clone()
        img=img.squeeze(0)
        img=fc(img)
        return img


    def img_save(img,path:str,name:str):
        path=os.path.join(path,name)
        img.save(path)
        print("image saved as: ",path)

    
