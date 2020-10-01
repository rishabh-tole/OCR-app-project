'use strict';

const { createWorker } = require('tesseract.js');
const _fs = require('fs');

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
//const image = _fs.readFileSync('./demo.png');

// Provide path to image on the internet
const image = 'https://pyimagesearch.com/wp-content/uploads/2017/06/example_01.png';

extractText(image).then((text) => {
    console.log('------------------------');
    console.log('OCR completed');
    console.log('------------------------');
    console.log(text);
    console.log('------------------------');
});

