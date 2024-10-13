import * as pdfjsLib from './pdf.min.mjs';
pdfjsLib.GlobalWorkerOptions.workerSrc = './pdf.worker.mjs';

document.getElementById('input-file').addEventListener('change', function (event) {
  const file = event.target.files[0];
  if (file && file.type === 'application/pdf') {
    const reader = new FileReader();
    reader.onload = function (e) {
      const pdfData = new Uint8Array(e.target.result);
      pdfjsLib.getDocument({ data: pdfData }).promise.then(function (pdf) {
        pdf.getPage(1).then(function (page) {
          const scale = 1.5;
          const viewport = page.getViewport({ scale: scale });
          const canvas = document.getElementById('showPDF');
          const context = canvas.getContext('2d');
          context.clearRect(0, 0, canvas.width, canvas.height);
          canvas.height = viewport.height;
          canvas.width = viewport.width;
          canvas.style.display = 'block';
          const renderContext = {
            canvasContext: context,
            viewport: viewport
          };
          page.render(renderContext);
        });
      });
    };
    reader.readAsArrayBuffer(file);
  }
});

const btn_delet = document.getElementById('btn_delete').addEventListener('click', function () {
  const canvas = document.getElementById('showPDF')
  const context = canvas.getContext('2d')
  context.clearRect(0, 0, canvas.width, canvas.height)
  canvas.style.display = 'block'
});
