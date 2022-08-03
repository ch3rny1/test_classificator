const ort = require('onnxruntime-web');

// create an inference session, using WebGL backend. (default is 'wasm')
const session = await ort.InferenceSession.create('./model.onnx', { executionProviders: ['webgl'] });
…
// feed inputs and run
const results = await session.run(feeds);

// set maximum thread number for WebAssembly backend. Setting to 1 to disable multi-threads
ort.wasm.numThreads = 1;

// set flag to enable/disable SIMD (default is true)
ort.wasm.simd = false;
