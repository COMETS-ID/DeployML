# Machine Learning Deployment Using  Flask

## Folder Structure
- `.dockerignore`
- `Dockerfile` -> for installing requirements
- `main.py` -> for running Flask
- `model10.h5` -> fixed model ML to be loaded
- `requirements.txt` -> required libraries
  
## Requirements
- Make sure your have installed any Python version
- Install all libraries from `requirements.txt`
- Install docker extension in VSCode

## Running and Testing Model on Postman
- Open the folder in VSCode
- Ensure all requirements have been installed
- Run 'python main.py' in the terminal, the ouput will be displayed url link
- Create a workspace in Postman and set the methods with 'POST' and copy the URL link
- Setting the body with key type File and fill with 'file' variable
- Upload the test image, click send, and if the test success will return the model prediction

## Notes
- Before test your image, make sure you have already adjusted the input shape on 'main.py'
- You can check the input shape of your model using [netron.app](https://netron.app/)https://netron.app/
  
