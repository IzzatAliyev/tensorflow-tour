# Tensorflow tour 

## 1. Create a Virtual Environment
Open a terminal or command prompt and navigate to the directory where you want to create your virtual environment. Then, run the following commands:

# On Windows
`python -m venv venv`

# On macOS/Linux
`python3 -m venv venv`

This will create a virtual environment named "venv" in your current directory.

## 2. Activate the Virtual Environment
Activate the virtual environment. The commands vary depending on your operating system:

On Windows:

`venv\Scripts\activate`

On macOS/Linux:

`source venv/bin/activate`

You should see the virtual environment's name in your command prompt or terminal prompt, indicating that the virtual environment is active.

## 3. Install TensorFlow
With the virtual environment activated, you can now install TensorFlow using pip:

`pip install tensorflow`

This will install the latest version of TensorFlow within your virtual environment.

## 4. Verify Installation
You can verify that TensorFlow is installed correctly by running the following Python code within the virtual environment:

```
import tensorflow as tf

print("TensorFlow version:", tf.__version__)
```

# Test TensorFlow by creating a simple tensor
```
tensor = tf.constant("Hello, TensorFlow!")
print(tensor)
```
## 5. Start Coding
Now you can start coding with TensorFlow in your virtual environment. You can use your favorite code editor or IDE to create and run TensorFlow programs.

Remember to activate the virtual environment whenever you want to work on your TensorFlow project:

# On Windows
`venv\Scripts\activate`

# On macOS/Linux
`source venv/bin/activate`

## 6. Deactivate the Virtual Environment
When you're done working in your virtual environment, you can deactivate it using the following command:

```deactivate```

This will return you to the global Python environment.