# SamskrutaASR

Speech to text for Samskruta

This project has two parts.
1. Training a Deep Learning model using Samskruta labelled Speech data.
2. Developing a Flask Application and hosting it on Azure Cloud Platform.
   
<br>

### **Skills you can gain by doing this Project:** *(Its a better way of writing 'Prerequisites', as 'Learn while doing a Project' is better than 'Learn and then do a Project')*
<br>

#### **Without Deep Learning:**

You can use the given (or any) trained Model and build the interactive application.
You will learn:
1. Flask
2. HTML, CSS, Javascript
3. Bash scripting
4. Docker
5. Azure Cloud Platform with Visual Studio Code

#### **With Deep Learning:**

You can train a ASR model for any Indian Language, and build an interactive application.
Requirements: Labelled Dataset of the language of your choice and GPU for Model training.
Note: This is not tinyML, so Graphics card in Laptop is not enough, atleast 8-10 GB of GPU is required if you use the Pre-trained model that I have mentioned.
So, along with skills mentioned in the previous section, you can learn,
1. Deep Learning
2. Self-Supervised learning
3. Handling huge datasets and using GPU.
4. Some knowledge in Speech Processing.



### **1. Model Training:**

I have referred work done by vakyansh team for training the model. - https://github.com/Open-Speech-EkStep/vakyansh-wav2vec2-experimentation/tree/ieee

Link for the trained model: https://drive.google.com/file/d/1Sa9WCXOE7VHcob4fyB0tzekOD-OfOz-9/view?usp=sharing


### **2. Flask Application:**

Link to the application : https://asr.sambhasha.ksu.ac.in

Following files/folders are involved: 
1. app.py - Main python file
2. templates - Directory containing HTML files
3. static - Directory containing CSS and JS (JavaScript) files
4. single_file_inference.py - Function that takes in audio as input and gives transcript (text) as output

### **3. Building Docker Image and hosting it on Azure**

I prefer using Visual Studio Code, as it has extensions for Docker and Azure.

1. **Creating Dockerfile**
    * I am using a pytorch base image and installing other required packages on top of it. An ubuntu base image can also be used and in that case pytorch should be installed on top of it.
    * Work directory is set and files and folders are copied from source to the destination path in the image's filesystem.
    * The network port that this container will listen on at runtime is defined.
    * Container is configured to be run as an executable.

<br>

2. **Using Azure to host the application**
   * Azure for students - https://azure.microsoft.com/en-us/free/students/ has free credits. Check with .edu mail id.
   * Create a container registry
   * Sign in to Azure in VS Code
   * Authenticate using following commands in VS code terminal.
        - az login
        - az acr login --name *'acrName'*
   * Build docker image from the dockerfile
   * Deploy the image to container registry
   * Deploy to Azure app service
   * Add port value in settings in Azure
   * Select a suitable app service plan - For the model used here, I opted for 8GB RAM. 
  
**Note:** *Check references for detailed instructions about hosting on Azure.*

#### **References:**

1. Vakyansh - https://github.com/Open-Speech-EkStep/vakyansh-wav2vec2-experimentation/tree/ieee
2. CS50 (For learning Flask) - https://www.youtube.com/watch?v=oVA0fD13NGI 
3. Running a custom container on Azure - https://learn.microsoft.com/en-gb/azure/app-service/quickstart-custom-container?pivots=container-linux-vscode&tabs=python
4. Authenticate with an Azure container registry - https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication?tabs=azure-cli