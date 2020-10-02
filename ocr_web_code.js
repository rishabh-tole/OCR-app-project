'use strict';

const { createWorker } = require('tesseract.js');
const _fs = require('fs');

var files = _fs.readdirSync('/Users/phinix/Desktop/OCR');


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

    //Return results
    return text;
}

// This can be a string or actual image data.

// Read image data from file system
const image = _fs.readFileSync('/Users/phinix/Desktop/OCR/' + files[1]);

//if want adress = take out fs.readfile

// Provide path to image on the internet







extractText(image).then((text) => {
    console.log('------------------------');
    console.log('OCR completed');
    console.log('------------------------');
    console.log(text);
    console.log('------------------------');
});

