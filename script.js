console.log('Hello TensorFlow');
const webcamElement = document.getElementById('webcam');

let net;

async function app() {
  console.log('Loading mobilenet..');

  // Load the model.
  const model = await tf.loadLayersModel('https://api.jsonbin.io/b/5f10169c9180616628429b21');
  console.log('Successfully loaded model');
  
  // Create an object from Tensorflow.js data API which could capture image 
  // from the web camera as Tensor.
  const webcam = await tf.data.webcam(webcamElement);
  while (true) {
    const img = await webcam.capture();
    const result = model.predict(img);

    document.getElementById('console').innerText = result;
    // Dispose the tensor to release the memory.
    img.dispose();

    // Give some breathing room by waiting for the next animation frame to
    // fire.
    await tf.nextFrame();
  }
}


app();