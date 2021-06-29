'use strict';
const { createWorker } = require('tesseract.js');
const _fs = require('fs');

//var files = _fs.readdirSync('/Users/phinix/Desktop/OCR');


async function call(){
  console.log(" ")
}
async function extractText(image) {
    console.log('Creating worker');
    const worker = createWorker();

    // Initialize the worker
    console.log('Initializing worker');
    await worker.load();
    await worker.loadLanguage('eng');
    await worker.initialize('eng');

    // Ask the worker to perform OCR on the image
    console.log('Performing OCR');
    const { data: { text } } = await worker.recognize(image);

    //Close the worker
    console.log('Terminating worker');
    await worker.terminate();

    _fs.writeFile('document.txt', text, call);
    return text;
}



//This can be a string or actual image data.

// Read image data from file system

//const image = _fs.readFileSync('/Users/phinix/Desktop/OCR/' + files[1]);

const image = _fs.readFileSync("testocr.png")

//if want adress = take out fs.readfile

// Provide path to image on the internet







extractText(image).then((text) => {
    console.log("text");
});

